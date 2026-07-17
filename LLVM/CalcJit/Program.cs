using System;
using System.Runtime.InteropServices;
using LLVMSharp;
using LLVMSharp.Interop;

namespace CalcJit
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 1. Проверка аргументов командной строки
            if (args.Length == 0)
            {
                Console.WriteLine("Usage: CalcJit \"expression\"");
                Console.WriteLine("Example: CalcJit \"3 + 4 * 2\"");
                return;
            }

            string expr = args[0];

            // 2. Инициализация всех целевых компонентов LLVM (необходимо для JIT)
            LLVM.InitializeAllTargets();
            LLVM.InitializeAllTargetInfos();
            LLVM.InitializeAllTargetMCs();
            LLVM.InitializeAllAsmPrinters();

            // 3. Создание контекста, модуля и билдера
            var context = LLVM.ContextCreate();                               // контекст – хранит типы, константы и т.д.
            var module = LLVM.ModuleCreateWithNameInContext("calc", context); // модуль – единица компиляции
            var builder = LLVM.CreateBuilderInContext(context);              // билдер – для вставки инструкций

            // 4. Установка целевой платформы (триплет)
            string targetTriple = LLVM.GetDefaultTargetTriple();
            LLVM.SetTarget(module, targetTriple); // задаём архитектуру (например, x86_64-pc-windows-msvc)

            // 5. Создание функции main (int main(int argc, char** argv))
            //    Тип функции: i32 (int) с двумя аргументами: i32 и i8**
            var mainType = LLVM.FunctionType(
                LLVM.Int32Type(),
                new[] { LLVM.Int32Type(), LLVM.PointerType(LLVM.Int8Type(), 0) },
                false); // false – не vararg
            var mainFunc = LLVM.AddFunction(module, "main", mainType);

            // 6. Создание базового блока и позиционирование билдера
            var entry = LLVM.AppendBasicBlock(mainFunc, "entry");
            LLVM.PositionBuilderAtEnd(builder, entry);

            // 7. Парсинг арифметического выражения в AST
            var parser = new Parser(expr);
            var ast = parser.ParseExpression();

            // 8. Генерация LLVM IR из AST
            var generator = new CodeGenerator(builder);
            LLVMValueRef resultValue = generator.Generate(ast);

            // 9. Инструкция возврата из main
            LLVM.BuildRet(builder, resultValue);

            // 10. Верификация модуля (проверка на ошибки)
            string errorMessage;
            if (LLVM.VerifyModule(module, LLVMVerifierFailureAction.LLVMPrintMessageAction, out errorMessage))
            {
                Console.WriteLine("Ошибка верификации модуля:");
                Console.WriteLine(errorMessage);
                return;
            }

            // 11. Создание JIT-компилятора (MCJIT)
            string jitError;
            var engine = LLVM.CreateMCJITCompilerForModule(module, out jitError);
            if (engine == null)
            {
                Console.WriteLine("Ошибка создания JIT-компилятора: " + jitError);
                return;
            }

            // 12. Получение указателя на скомпилированную функцию main
            IntPtr mainPtr = LLVM.GetPointerToGlobal(engine, mainFunc);
            if (mainPtr == IntPtr.Zero)
            {
                Console.WriteLine("Не удалось получить указатель на функцию main");
                return;
            }

            // 13. Преобразование указателя в делегат и вызов
            var mainDelegate = Marshal.GetDelegateForFunctionPointer<MainDelegate>(mainPtr);
            int result = mainDelegate(0, IntPtr.Zero); // argc=0, argv=null (не используются)

            // 14. Вывод результата
            Console.WriteLine($"Результат: {result}");

            // 15. Освобождение ресурсов (рекомендуется)
            LLVM.DisposeMCJITCompiler(engine);
            LLVM.DisposeBuilder(builder);
            LLVM.DisposeModule(module);
            LLVM.ContextDispose(context);
        }

        // Делегат для вызова скомпилированной функции main
        private delegate int MainDelegate(int argc, IntPtr argv);
    }

    // ---------- Абстрактное синтаксическое дерево (AST) ----------
    public abstract class ExprNode { }

    public class NumberNode : ExprNode
    {
        public int Value { get; }
        public NumberNode(int value) => Value = value;
    }

    public class BinaryOpNode : ExprNode
    {
        public char Op { get; }
        public ExprNode Left { get; }
        public ExprNode Right { get; }
        public BinaryOpNode(char op, ExprNode left, ExprNode right)
        {
            Op = op;
            Left = left;
            Right = right;
        }
    }

    // ---------- Рекурсивный парсер (поддерживает +, -, *, / и скобки) ----------
    public class Parser
    {
        private readonly string _input;
        private int _pos;

        public Parser(string input) => _input = input;

        private char Peek() => _pos < _input.Length ? _input[_pos] : '\0';
        private char Next() => _pos < _input.Length ? _input[_pos++] : '\0';
        private void SkipWhitespace()
        {
            while (char.IsWhiteSpace(Peek()))
                Next();
        }

        // expr := term (('+' | '-') term)*
        public ExprNode ParseExpression()
        {
            var left = ParseTerm();
            while (true)
            {
                SkipWhitespace();
                char op = Peek();
                if (op != '+' && op != '-')
                    break;
                Next();
                var right = ParseTerm();
                left = new BinaryOpNode(op, left, right);
            }
            return left;
        }

        // term := factor (('*' | '/') factor)*
        private ExprNode ParseTerm()
        {
            var left = ParseFactor();
            while (true)
            {
                SkipWhitespace();
                char op = Peek();
                if (op != '*' && op != '/')
                    break;
                Next();
                var right = ParseFactor();
                left = new BinaryOpNode(op, left, right);
            }
            return left;
        }

        // factor := number | '(' expr ')'
        private ExprNode ParseFactor()
        {
            SkipWhitespace();
            if (Peek() == '(')
            {
                Next(); // пропускаем '('
                var node = ParseExpression();
                SkipWhitespace();
                if (Peek() != ')')
                    throw new Exception("Ожидается ')'");
                Next(); // пропускаем ')'
                return node;
            }

            if (char.IsDigit(Peek()))
            {
                int value = 0;
                while (char.IsDigit(Peek()))
                {
                    value = value * 10 + (Peek() - '0');
                    Next();
                }
                return new NumberNode(value);
            }

            throw new Exception($"Неожиданный символ: {Peek()}");
        }
    }

    // ---------- Генератор LLVM IR по AST ----------
    public class CodeGenerator
    {
        private readonly LLVMBuilderRef _builder;

        public CodeGenerator(LLVMBuilderRef builder)
        {
            _builder = builder;
        }

        public LLVMValueRef Generate(ExprNode node)
        {
            return node switch
            {
                NumberNode num => LLVM.ConstInt(LLVM.Int32Type(), (ulong)num.Value, false),
                BinaryOpNode bin => GenerateBinaryOp(bin),
                _ => throw new Exception("Неизвестный узел AST")
            };
        }

        private LLVMValueRef GenerateBinaryOp(BinaryOpNode bin)
        {
            var left = Generate(bin.Left);
            var right = Generate(bin.Right);

            return bin.Op switch
            {
                '+' => LLVM.BuildAdd(_builder, left, right, "addtmp"),
                '-' => LLVM.BuildSub(_builder, left, right, "subtmp"),
                '*' => LLVM.BuildMul(_builder, left, right, "multmp"),
                '/' => LLVM.BuildSDiv(_builder, left, right, "divtmp"),
                _ => throw new Exception($"Неизвестный оператор: {bin.Op}")
            };
        }
    }
}