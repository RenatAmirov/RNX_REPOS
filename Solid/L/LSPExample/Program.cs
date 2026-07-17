using System;
using System.Collections.Generic;
using System.Linq;

namespace LSPExample
{
    // =========================================================================
    //  ЧАСТЬ 1. НАРУШЕНИЕ ПРИНЦИПА ПОДСТАНОВКИ ЛИСКОВ (LSP)
    // =========================================================================

    /// <summary>
    /// Интерфейс, определяющий операции чтения и записи настроек.
    /// Этот интерфейс нарушает LSP, потому что некоторые классы не могут
    /// реализовать запись (SetSettings) без выбрасывания исключения.
    /// </summary>
    public interface ISettings
    {
        Dictionary<string, string> GetSettings();
        string SetSettings(Dictionary<string, string> settings);
    }

    /// <summary>
    /// Глобальные настройки – поддерживают и чтение, и запись.
    /// </summary>
    public class GlobalSettings : ISettings
    {
        // Имитация хранения данных в словаре
        private Dictionary<string, string> _data = new Dictionary<string, string>
        {
            ["Theme"] = "Summer"
        };

        public Dictionary<string, string> GetSettings()
        {
            // Возвращаем копию данных, чтобы внешний код не мог их изменить напрямую
            return new Dictionary<string, string>(_data);
        }

        public string SetSettings(Dictionary<string, string> settings)
        {
            // Обновляем данные из переданного словаря
            foreach (var kvp in settings)
                _data[kvp.Key] = kvp.Value;
            return $"Global settings updated at {DateTime.Now}";
        }
    }

    /// <summary>
    /// Настройки раздела – поддерживают и чтение, и запись.
    /// </summary>
    public class SectionSettings : ISettings
    {
        private Dictionary<string, string> _data = new Dictionary<string, string>
        {
            ["Title"] = "Sports"
        };

        public Dictionary<string, string> GetSettings() => new Dictionary<string, string>(_data);
        public string SetSettings(Dictionary<string, string> settings)
        {
            foreach (var kvp in settings)
                _data[kvp.Key] = kvp.Value;
            return $"Section settings updated at {DateTime.Now}";
        }
    }

    /// <summary>
    /// Настройки пользователя – поддерживают и чтение, и запись.
    /// </summary>
    public class UserSettings : ISettings
    {
        private Dictionary<string, string> _data = new Dictionary<string, string>
        {
            ["DisplayName"] = "User1"
        };

        public Dictionary<string, string> GetSettings() => new Dictionary<string, string>(_data);
        public string SetSettings(Dictionary<string, string> settings)
        {
            foreach (var kvp in settings)
                _data[kvp.Key] = kvp.Value;
            return $"User settings updated at {DateTime.Now}";
        }
    }

    /// <summary>
    /// Настройки гостевого пользователя – могут читать настройки, но НЕ могут их сохранять.
    /// Этот класс НАРУШАЕТ LSP, потому что он реализует интерфейс ISettings,
    /// но метод SetSettings выбрасывает исключение.
    /// Клиентский код, ожидающий ISettings, не должен получать исключение при вызове SetSettings.
    /// </summary>
    public class GuestSettings : ISettings
    {
        private Dictionary<string, string> _data = new Dictionary<string, string>
        {
            ["GuestName"] = "John"
        };

        public Dictionary<string, string> GetSettings() => new Dictionary<string, string>(_data);

        // НАРУШЕНИЕ LSP: гость не может сохранять настройки,
        // но интерфейс обязывает реализовать этот метод.
        public string SetSettings(Dictionary<string, string> settings)
        {
            throw new NotImplementedException("Гостевые пользователи не могут изменять настройки!");
        }
    }

    /// <summary>
    /// Вспомогательный класс, который работает со списком объектов ISettings.
    /// Он полагается на то, что все объекты корректно реализуют и GetSettings, и SetSettings.
    /// При наличии GuestSettings этот класс вызовет исключение.
    /// </summary>
    public static class SettingsHelper
    {
        /// <summary>
        /// Получает все настройки из списка объектов ISettings.
        /// </summary>
        public static Dictionary<ISettings, Dictionary<string, string>> GetAllSettings(List<ISettings> items)
        {
            var result = new Dictionary<ISettings, Dictionary<string, string>>();
            foreach (var item in items)
            {
                result.Add(item, item.GetSettings());
            }
            return result;
        }

        /// <summary>
        /// Сохраняет переданные настройки в каждый объект ISettings.
        /// Если среди объектов есть GuestSettings, этот метод выбросит исключение.
        /// </summary>
        public static List<string> SetAllSettings(List<ISettings> items, List<Dictionary<string, string>> values)
        {
            var messages = new List<string>();
            for (int i = 0; i < items.Count; i++)
            {
                // Здесь вызовется SetSettings у GuestSettings -> исключение
                messages.Add(items[i].SetSettings(values[i]));
            }
            return messages;
        }
    }


    // =========================================================================
    //  ЧАСТЬ 2. ИСПРАВЛЕНИЕ – РАЗДЕЛЕНИЕ ИНТЕРФЕЙСОВ (СОБЛЮДЕНИЕ LSP)
    // =========================================================================

    /// <summary>
    /// Интерфейс только для чтения настроек.
    /// </summary>
    public interface IReadableSettings
    {
        Dictionary<string, string> GetSettings();
    }

    /// <summary>
    /// Интерфейс только для записи настроек.
    /// </summary>
    public interface IWritableSettings
    {
        string SetSettings(Dictionary<string, string> settings);
    }

    /// <summary>
    /// Глобальные настройки (исправленная версия) – поддерживают и чтение, и запись.
    /// </summary>
    public class GlobalSettingsFixed : IReadableSettings, IWritableSettings
    {
        private Dictionary<string, string> _data = new Dictionary<string, string> { ["Theme"] = "Summer" };

        public Dictionary<string, string> GetSettings() => new Dictionary<string, string>(_data);

        public string SetSettings(Dictionary<string, string> settings)
        {
            foreach (var kvp in settings)
                _data[kvp.Key] = kvp.Value;
            return $"Global settings updated (fixed) at {DateTime.Now}";
        }
    }

    /// <summary>
    /// Настройки раздела (исправленная версия).
    /// </summary>
    public class SectionSettingsFixed : IReadableSettings, IWritableSettings
    {
        private Dictionary<string, string> _data = new Dictionary<string, string> { ["Title"] = "Sports" };

        public Dictionary<string, string> GetSettings() => new Dictionary<string, string>(_data);
        public string SetSettings(Dictionary<string, string> settings)
        {
            foreach (var kvp in settings)
                _data[kvp.Key] = kvp.Value;
            return $"Section settings updated (fixed) at {DateTime.Now}";
        }
    }

    /// <summary>
    /// Настройки пользователя (исправленная версия).
    /// </summary>
    public class UserSettingsFixed : IReadableSettings, IWritableSettings
    {
        private Dictionary<string, string> _data = new Dictionary<string, string> { ["DisplayName"] = "User1" };

        public Dictionary<string, string> GetSettings() => new Dictionary<string, string>(_data);
        public string SetSettings(Dictionary<string, string> settings)
        {
            foreach (var kvp in settings)
                _data[kvp.Key] = kvp.Value;
            return $"User settings updated (fixed) at {DateTime.Now}";
        }
    }

    /// <summary>
    /// Гостевые настройки (исправленная версия) – теперь реализуют ТОЛЬКО чтение.
    /// Это корректно, потому что они не обязаны реализовывать запись.
    /// LSP соблюдён: объект GuestSettingsFixed можно использовать везде,
    /// где ожидается IReadableSettings, и он не выбросит исключение.
    /// </summary>
    public class GuestSettingsFixed : IReadableSettings
    {
        private Dictionary<string, string> _data = new Dictionary<string, string> { ["GuestName"] = "John" };

        public Dictionary<string, string> GetSettings() => new Dictionary<string, string>(_data);
        // Метод SetSettings отсутствует – это правильно, так как интерфейс IReadableSettings его не требует.
    }

    /// <summary>
    /// Вспомогательный класс (исправленная версия), работающий с разделёнными интерфейсами.
    /// </summary>
    public static class SettingsHelperFixed
    {
        /// <summary>
        /// Получает настройки только от объектов, реализующих IReadableSettings.
        /// Сюда можно передавать и GuestSettingsFixed, и всё будет работать.
        /// </summary>
        public static Dictionary<IReadableSettings, Dictionary<string, string>> GetAllSettings(List<IReadableSettings> items)
        {
            var result = new Dictionary<IReadableSettings, Dictionary<string, string>>();
            foreach (var item in items)
            {
                result.Add(item, item.GetSettings());
            }
            return result;
        }

        /// <summary>
        /// Сохраняет настройки только в объекты, реализующие IWritableSettings.
        /// GuestSettingsFixed не передаются сюда, поэтому исключений не будет.
        /// </summary>
        public static List<string> SetAllSettings(List<IWritableSettings> items, List<Dictionary<string, string>> values)
        {
            var messages = new List<string>();
            for (int i = 0; i < items.Count; i++)
            {
                messages.Add(items[i].SetSettings(values[i]));
            }
            return messages;
        }
    }


    // =========================================================================
    //  ГЛАВНАЯ ПРОГРАММА
    // =========================================================================

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация принципа подстановки Лисков (LSP) ===\n");

            // ---- ЧАСТЬ 1: НАРУШЕНИЕ LSP ----
            Console.WriteLine("--- ЧАСТЬ 1: Нарушение LSP ---");

            // Создаём список объектов ISettings, включая GuestSettings
            List<ISettings> settingsList = new List<ISettings>
            {
                new GlobalSettings(),
                new SectionSettings(),
                new UserSettings(),
                new GuestSettings() // <- нарушитель
            };

            // Получение настроек работает для всех объектов (включая GuestSettings)
            Console.WriteLine("Получение настроек (GetAllSettings):");
            var allSettings = SettingsHelper.GetAllSettings(settingsList);
            foreach (var kvp in allSettings)
            {
                Console.WriteLine($"  {kvp.Key.GetType().Name}: {string.Join(", ", kvp.Value.Select(p => $"{p.Key}={p.Value}"))}");
            }

            // Попытка сохранить настройки – вызовет исключение из-за GuestSettings
            Console.WriteLine("\nПопытка сохранить настройки (SetAllSettings)...");
            try
            {
                // Подготавливаем новые значения для каждого объекта (по одному словарю на каждый)
                List<Dictionary<string, string>> newSettings = new List<Dictionary<string, string>>
                {
                    new Dictionary<string, string> { ["Theme"] = "Winter" },
                    new Dictionary<string, string> { ["Title"] = "Music" },
                    new Dictionary<string, string> { ["DisplayName"] = "Tom" },
                    new Dictionary<string, string> { ["GuestName"] = "Jerry" } // для GuestSettings
                };

                var messages = SettingsHelper.SetAllSettings(settingsList, newSettings);
                Console.WriteLine("Результаты сохранения:");
                foreach (var msg in messages)
                    Console.WriteLine($"  {msg}");
            }
            catch (NotImplementedException ex)
            {
                Console.WriteLine($"ОШИБКА: {ex.Message}");
                Console.WriteLine("Это происходит потому, что GuestSettings не может реализовать SetSettings,");
                Console.WriteLine("но интерфейс ISettings требует этого – нарушение LSP.\n");
            }

            // ---- ЧАСТЬ 2: ИСПРАВЛЕНИЕ (СОБЛЮДЕНИЕ LSP) ----
            Console.WriteLine("\n--- ЧАСТЬ 2: Исправление (разделение интерфейсов) ---");

            // Создаём списки объектов с разделёнными интерфейсами
            List<IReadableSettings> readableList = new List<IReadableSettings>
            {
                new GlobalSettingsFixed(),
                new SectionSettingsFixed(),
                new UserSettingsFixed(),
                new GuestSettingsFixed() // теперь реализует только IReadableSettings
            };

            List<IWritableSettings> writableList = new List<IWritableSettings>
            {
                new GlobalSettingsFixed(),
                new SectionSettingsFixed(),
                new UserSettingsFixed()
                // GuestSettingsFixed отсутствует – он не может быть записан, что логично
            };

            // Чтение настроек работает со всеми, включая гостя
            Console.WriteLine("Получение настроек (исправленная версия):");
            var allSettingsFixed = SettingsHelperFixed.GetAllSettings(readableList);
            foreach (var kvp in allSettingsFixed)
            {
                Console.WriteLine($"  {kvp.Key.GetType().Name}: {string.Join(", ", kvp.Value.Select(p => $"{p.Key}={p.Value}"))}");
            }

            // Сохранение настроек – теперь только для объектов, поддерживающих запись
            Console.WriteLine("\nСохранение настроек (исправленная версия):");
            List<Dictionary<string, string>> newSettingsFixed = new List<Dictionary<string, string>>
            {
                new Dictionary<string, string> { ["Theme"] = "Winter" },
                new Dictionary<string, string> { ["Title"] = "Music" },
                new Dictionary<string, string> { ["DisplayName"] = "Tom" }
            };

            var messagesFixed = SettingsHelperFixed.SetAllSettings(writableList, newSettingsFixed);
            foreach (var msg in messagesFixed)
                Console.WriteLine($"  {msg}");

            Console.WriteLine("\nВсе операции выполнены успешно. LSP соблюдён!");
            Console.WriteLine("Нажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}