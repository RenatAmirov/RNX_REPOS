namespace DIP_Example
{
    using System;

    // ============================================================
    // Пример, иллюстрирующий Принцип инверсии зависимостей (DIP)
    // из книги "Beginning SOLID Principles and Design Patterns for ASP.NET Developers"
    // ============================================================

    // 1. Определяем абстракцию (интерфейс) для уведомлений.
    //    Модули верхнего уровня (UserManager) будут зависеть от этой абстракции,
    //    а не от конкретных реализаций.
    public interface INotifier
    {
        void Notify(string message);
    }

    // 2. Реализуем конкретные классы уведомлений (низкоуровневые модули).
    //    Они реализуют интерфейс INotifier – следуем принципу DIP.

    // Уведомление по электронной почте
    public class EmailNotifier : INotifier
    {
        public void Notify(string message)
        {
            // Здесь могла бы быть реальная отправка email,
            // но для примера просто выводим в консоль.
            Console.WriteLine($"Email уведомление: {message}");
        }
    }

    // Уведомление через SMS
    public class SmsNotifier : INotifier
    {
        public void Notify(string message)
        {
            Console.WriteLine($"SMS уведомление: {message}");
        }
    }

    // Уведомление через всплывающее окно (Popup)
    public class PopupNotifier : INotifier
    {
        public void Notify(string message)
        {
            Console.WriteLine($"Popup уведомление: {message}");
        }
    }

    // 3. Создаём высокоуровневый модуль (UserManager),
    //    который управляет пользователями и отправляет уведомления.
    //    Он НЕ зависит от конкретных классов (EmailNotifier, SmsNotifier и т.д.),
    //    а зависит от абстракции INotifier.
    //    Это позволяет легко подменять способ уведомления без изменения кода UserManager.
    public class UserManager
    {
        // Поле для хранения ссылки на абстракцию уведомлений
        private readonly INotifier _notifier;

        // Внедрение зависимости через конструктор (Dependency Injection).
        // Это позволяет передавать любую реализацию INotifier извне.
        public UserManager(INotifier notifier)
        {
            _notifier = notifier ?? throw new ArgumentNullException(nameof(notifier));
        }

        // Метод смены пароля.
        // После выполнения операции отправляет уведомление через внедрённый notifier.
        public void ChangePassword(string username, string oldPassword, string newPassword)
        {
            // Здесь должна быть реальная логика смены пароля,
            // но для примера просто выводим сообщение.
            Console.WriteLine($"Пароль для пользователя {username} был изменён.");

            // Отправляем уведомление о смене пароля.
            // Мы не знаем, какой именно notifier используется – это зависит от того,
            // что было передано в конструктор.
            _notifier.Notify($"Пароль для {username} был изменён в {DateTime.Now}");
        }
    }

    // 4. Главный класс программы (точка входа).
    //    Здесь мы демонстрируем, как легко можно подставлять разные реализации
    //    уведомлений, не меняя код UserManager.
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация принципа инверсии зависимостей (DIP) ===\n");

            // Пример 1: используем EmailNotifier.
            Console.WriteLine("1. Используем EmailNotifier:");
            INotifier emailNotifier = new EmailNotifier();
            UserManager userManagerWithEmail = new UserManager(emailNotifier);
            userManagerWithEmail.ChangePassword("alice", "oldPass123", "newPass456");
            Console.WriteLine();

            // Пример 2: используем SmsNotifier.
            Console.WriteLine("2. Используем SmsNotifier:");
            INotifier smsNotifier = new SmsNotifier();
            UserManager userManagerWithSms = new UserManager(smsNotifier);
            userManagerWithSms.ChangePassword("bob", "qwerty", "123456");
            Console.WriteLine();

            // Пример 3: используем PopupNotifier.
            Console.WriteLine("3. Используем PopupNotifier:");
            INotifier popupNotifier = new PopupNotifier();
            UserManager userManagerWithPopup = new UserManager(popupNotifier);
            userManagerWithPopup.ChangePassword("charlie", "letmein", "securePass");
            Console.WriteLine();

            // Мы можем даже создать фабрику или использовать конфигурацию,
            // чтобы выбирать способ уведомления динамически.
            // Главное – UserManager не зависит от конкретных классов,
            // что делает систему гибкой и легко расширяемой.

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}
