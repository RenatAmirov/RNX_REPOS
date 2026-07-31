namespace EventDemo
{
    class Program
    {
        static void Main()
        {
            var alarm = new AlarmClock();

            // Подписываемся на событие. Создаём обработчик.
            alarm.AlarmRang += (sender, e) =>
            {
                Console.WriteLine("Просыпаемся! Будильник сработал!");
            };

            // Симулируем срабатывание
            alarm.Ring();
        }
    }
}
