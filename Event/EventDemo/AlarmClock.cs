using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EventDemo
{
    public class AlarmClock
    {
        // Объявляем событие. Оно использует делегат EventHandler,
        // который принимает два параметра: отправителя и аргументы.
        public event EventHandler AlarmRang;

        public void SetAlarm(DateTime time)
        {
            // В реальном коде мы бы проверяли время в цикле или таймере.
            // Здесь просто имитируем срабатывание.
            Console.WriteLine($"Будильник установлен на {time}");
        }

        public void Ring()
        {
            // Проверяем, есть ли подписчики
            if (AlarmRang != null)
            {
                // Генерируем событие. Все подписчики получат уведомление.
                AlarmRang(this, EventArgs.Empty);
            }
        }
    }
}
