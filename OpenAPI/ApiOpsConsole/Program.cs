// ========================================================================
//   ПРОЕКТ: ApiOpsConsole
//   Описание: Демонстрация принципов APIOps на C# с использованием
//             спецификаций OpenAPI.
//   Требуемые пакеты NuGet (установить через консоль диспетчера пакетов):
//     Install-Package Microsoft.OpenApi -Version 1.6.14
//     Install-Package Microsoft.OpenApi.Readers -Version 1.6.14
//     Install-Package Microsoft.OpenApi.Yaml -Version 1.6.14
//   Альтернативно через .NET CLI:
//     dotnet add package Microsoft.OpenApi --version 1.6.14
//     dotnet add package Microsoft.OpenApi.Readers --version 1.6.14
//     dotnet add package Microsoft.OpenApi.Yaml --version 1.6.14
// ========================================================================

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.OpenApi;
using Microsoft.OpenApi.Models;
using Microsoft.OpenApi.Readers;
using Microsoft.OpenApi.Writers;

namespace ApiOpsConsole
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("=== APIOps: Автоматизация доставки API ===\n");

            string specFilePath = "api-spec.yaml";

            if (!File.Exists(specFilePath))
            {
                Console.WriteLine("Создание тестовой спецификации OpenAPI...");
                CreateSampleSpecification(specFilePath);
            }

            Console.WriteLine("Шаг 1: Загрузка спецификации OpenAPI...");
            var document = await LoadOpenApiSpecificationAsync(specFilePath);
            Console.WriteLine($"  Загружена: {document.Info.Title} (v{document.Info.Version})");

            Console.WriteLine("\nШаг 2: Линтинг и валидация спецификации...");
            var validationErrors = ValidateSpecification(document);
            if (validationErrors.Any())
            {
                Console.WriteLine("  Обнаружены ошибки:");
                foreach (var error in validationErrors)
                    Console.WriteLine($"    - {error}");
            }
            else
            {
                Console.WriteLine("  Спецификация прошла валидацию успешно.");
            }

            Console.WriteLine("\nШаг 3: Обнаружение критических изменений между версиями...");
            string oldSpec = "api-spec-v1.yaml";
            string newSpec = "api-spec-v2.yaml";
            if (!File.Exists(oldSpec))
                CreateSampleSpecification(oldSpec, version: "1.0.0");
            if (!File.Exists(newSpec))
                CreateSampleSpecification(newSpec, version: "2.0.0", withBreakingChange: true);

            var oldDoc = await LoadOpenApiSpecificationAsync(oldSpec);
            var newDoc = await LoadOpenApiSpecificationAsync(newSpec);

            var breakingChanges = DetectBreakingChanges(oldDoc, newDoc);
            if (breakingChanges.Any())
            {
                Console.WriteLine("  Обнаружены критические изменения:");
                foreach (var change in breakingChanges)
                    Console.WriteLine($"    - {change}");
            }
            else
            {
                Console.WriteLine("  Критических изменений не обнаружено.");
            }

            Console.WriteLine("\nШаг 4: Генерация клиентского SDK на C# (демонстрация)...");
            string clientCode = GenerateExampleClientCode(document);
            string outputDir = "GeneratedClient";
            if (!Directory.Exists(outputDir))
                Directory.CreateDirectory(outputDir);
            string clientFilePath = Path.Combine(outputDir, "ApiClient.g.cs");
            await File.WriteAllTextAsync(clientFilePath, clientCode);
            Console.WriteLine($"  Пример клиентского кода сохранён в {clientFilePath}");

            Console.WriteLine("\nШаг 5: Публикация документации API (симуляция)...");
            Console.WriteLine("  Документация может быть сгенерирована с помощью Swagger UI или Redoc.");
            Console.WriteLine("  В реальном проекте вы можете опубликовать её на портале разработчика.");

            Console.WriteLine("\n=== Завершено ===");
        }

        private static async Task<OpenApiDocument> LoadOpenApiSpecificationAsync(string filePath)
        {
            var yamlContent = await File.ReadAllTextAsync(filePath);
            using var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(yamlContent));
            var reader = new OpenApiStreamReader();
            var readResult = reader.Read(stream, out var document);

            //if (readResult.OpenApiDocument == null)
            //    throw new Exception("Не удалось прочитать спецификацию OpenAPI.");

            return document;
        }

        private static List<string> ValidateSpecification(OpenApiDocument doc)
        {
            var errors = new List<string>();

            if (doc.Info == null)
                errors.Add("Отсутствует объект 'info'.");
            else
            {
                if (string.IsNullOrEmpty(doc.Info.Title))
                    errors.Add("Отсутствует поле 'info.title'.");
                if (string.IsNullOrEmpty(doc.Info.Version))
                    errors.Add("Отсутствует поле 'info.version'.");
            }

            if (doc.Paths == null || doc.Paths.Count == 0)
                errors.Add("Отсутствуют пути (paths).");

            return errors;
        }

        private static List<string> DetectBreakingChanges(OpenApiDocument oldDoc, OpenApiDocument newDoc)
        {
            var changes = new List<string>();

            var oldPaths = oldDoc.Paths?.Select(p => p.Key).ToHashSet() ?? new HashSet<string>();
            var newPaths = newDoc.Paths?.Select(p => p.Key).ToHashSet() ?? new HashSet<string>();

            foreach (var removed in oldPaths.Except(newPaths))
                changes.Add($"Удалён путь '{removed}'.");

            if (oldDoc.Paths != null && newDoc.Paths != null)
            {
                foreach (var path in oldDoc.Paths.Keys.Intersect(newDoc.Paths.Keys))
                {
                    var oldOps = oldDoc.Paths[path].Operations;
                    var newOps = newDoc.Paths[path].Operations;

                    foreach (var opType in oldOps.Keys)
                    {
                        if (!newOps.ContainsKey(opType))
                            changes.Add($"Удалена операция {opType} для пути '{path}'.");
                    }
                }
            }

            return changes;
        }

        private static string GenerateExampleClientCode(OpenApiDocument doc)
        {
            var code = "// Автоматически сгенерированный клиент API (пример)\n";
            code += "// Для реальной генерации используйте NSwag или OpenAPI Generator.\n\n";
            code += "using System;\n";
            code += "using System.Net.Http;\n";
            code += "using System.Threading.Tasks;\n\n";
            code += "namespace ApiOpsClient\n{\n";
            code += "    public class ApiClient\n    {\n";
            code += "        private readonly HttpClient _httpClient;\n\n";
            code += "        public ApiClient(HttpClient httpClient)\n        {\n";
            code += "            _httpClient = httpClient;\n        }\n\n";

            if (doc.Paths != null)
            {
                foreach (var path in doc.Paths)
                {
                    foreach (var op in path.Value.Operations)
                    {
                        string methodName = op.Value.OperationId ?? $"{op.Key}{path.Key.Replace("/", "_").Replace("{", "").Replace("}", "")}";
                        methodName = char.ToUpper(methodName[0]) + methodName.Substring(1);
                        code += $"        // {op.Key} {path.Key}\n";
                        code += $"        public async Task<string> {methodName}Async()\n";
                        code += "        {\n";
                        code += $"            // TODO: реализовать вызов {op.Key} {path.Key}\n";
                        code += "            return await Task.FromResult(\"response\");\n";
                        code += "        }\n\n";
                    }
                }
            }

            code += "    }\n}\n";
            return code;
        }

        private static void CreateSampleSpecification(string filePath, string version = "1.0.0", bool withBreakingChange = false)
        {
            var doc = new OpenApiDocument
            {
                OpenApi = "3.0.1",
                Info = new OpenApiInfo
                {
                    Title = "Пример API каталога продуктов",
                    Version = version,
                    Description = "API для управления каталогом продуктов."
                },
                Servers = new List<OpenApiServer>
                {
                    new OpenApiServer { Url = "https://api.example.com/v1" }
                },
                Paths = new OpenApiPaths()
            };

            var getProducts = new OpenApiOperation
            {
                OperationId = "GetProducts",
                Summary = "Получить список продуктов",
                Responses = new OpenApiResponses
                {
                    { "200", new OpenApiResponse { Description = "Успешный ответ" } }
                }
            };

            if (withBreakingChange)
            {
                getProducts.OperationId = "CreateProduct";
                getProducts.Summary = "Создать продукт (изменение метода)";
                var pathItem = new OpenApiPathItem();
                pathItem.AddOperation(OperationType.Post, getProducts);
                doc.Paths.Add("/products", pathItem);
            }
            else
            {
                var pathItem = new OpenApiPathItem();
                pathItem.AddOperation(OperationType.Get, getProducts);
                doc.Paths.Add("/products", pathItem);
            }

            var getProductById = new OpenApiOperation
            {
                OperationId = "GetProductById",
                Summary = "Получить продукт по ID",
                Parameters = new List<OpenApiParameter>
                {
                    new OpenApiParameter
                    {
                        Name = "id",
                        In = ParameterLocation.Path,
                        Required = true,
                        Schema = new OpenApiSchema
                        {
                            Type = JsonSchemaType.String
                        }
                    }
                },
                Responses = new OpenApiResponses
                {
                    { "200", new OpenApiResponse { Description = "Успешный ответ" } },
                    { "404", new OpenApiResponse { Description = "Продукт не найден" } }
                }
            };
            var pathItem2 = new OpenApiPathItem();
            pathItem2.AddOperation(OperationType.Get, getProductById);
            doc.Paths.Add("/products/{id}", pathItem2);

            // Сериализация в YAML
            using var stringWriter = new StringWriter();
            var yamlWriter = new OpenApiYamlWriter(stringWriter);
            doc.SerializeAsV3(yamlWriter);
            var yaml = stringWriter.ToString();

            File.WriteAllText(filePath, yaml);
        }
    }
}