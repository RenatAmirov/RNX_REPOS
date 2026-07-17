using System;

namespace ISP_Example
{
    // =========================================================================
    //  ВСПОМОГАТЕЛЬНЫЕ КЛАССЫ (заглушки для данных)
    // =========================================================================
    public class Address { }
    public class CardInfo { }
    public class Order { }

    // =========================================================================
    //  ИНТЕРФЕЙСЫ, РАЗДЕЛЁННЫЕ СОГЛАСНО ISP
    // =========================================================================

    /// <summary>
    /// Базовый интерфейс для обработки заказов.
    /// Содержит методы, общие для всех способов оплаты.
    /// </summary>
    public interface IOrderProcessor
    {
        /// <summary> Проверка адреса доставки </summary>
        bool ValidateShippingAddress(Address address);

        /// <summary> Обработка заказа (списание товаров, создание накладной и т.п.) </summary>
        void ProcessOrder(Order order);
    }

    /// <summary>
    /// Дополнительный интерфейс для онлайн-платежей.
    /// Выделен в отдельный интерфейс, чтобы классы с оплатой при доставке
    /// не были вынуждены реализовывать ненужный метод.
    /// </summary>
    public interface IOnlineOrderProcessor
    {
        /// <summary> Проверка банковской карты </summary>
        bool ValidateCardInfo(CardInfo card);
    }

    // =========================================================================
    //  РЕАЛИЗАЦИИ (КОНКРЕТНЫЕ ОБРАБОТЧИКИ)
    // =========================================================================

    /// <summary>
    /// Обработчик онлайн-заказов (оплата картой).
    /// Реализует оба интерфейса – все методы ему нужны.
    /// </summary>
    public class OnlineOrderProcessor : IOrderProcessor, IOnlineOrderProcessor
    {
        public bool ValidateShippingAddress(Address address)
        {
            // Здесь могла бы быть сложная логика проверки адреса
            Console.WriteLine("  [Online] Проверка адреса доставки выполнена успешно.");
            return true;
        }

        public void ProcessOrder(Order order)
        {
            Console.WriteLine("  [Online] Заказ обработан (списание товаров, формирование накладной).");
        }

        public bool ValidateCardInfo(CardInfo card)
        {
            // Проверка карты через платёжный шлюз
            Console.WriteLine("  [Online] Данные карты проверены, платёж авторизован.");
            return true;
        }
    }

    /// <summary>
    /// Обработчик заказов с оплатой при доставке (наложенный платёж).
    /// Реализует только базовый интерфейс – метод ValidateCardInfo ему не нужен.
    /// </summary>
    public class CashOnDeliveryOrderProcessor : IOrderProcessor
    {
        public bool ValidateShippingAddress(Address address)
        {
            Console.WriteLine("  [COD] Проверка адреса доставки выполнена успешно.");
            return true;
        }

        public void ProcessOrder(Order order)
        {
            Console.WriteLine("  [COD] Заказ оформлен, оплата будет произведена при получении.");
        }
    }

    // =========================================================================
    //  КЛИЕНТСКИЙ КОД
    // =========================================================================

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("===== Демонстрация принципа разделения интерфейсов (ISP) =====\n");

            // --------------------------------------------------------------------
            // 1. Работа с онлайн-заказом
            // --------------------------------------------------------------------
            Console.WriteLine("--- 1. Онлайн-заказ (оплата картой) ---");
            IOrderProcessor onlineOrder = new OnlineOrderProcessor();

            // Вызов общих методов (доступны через базовый интерфейс)
            onlineOrder.ValidateShippingAddress(new Address());
            onlineOrder.ProcessOrder(new Order());

            // Для проверки карты требуется привести объект к интерфейсу IOnlineOrderProcessor
            // Это безопасно, потому что OnlineOrderProcessor реализует этот интерфейс.
            var onlineWithCard = onlineOrder as IOnlineOrderProcessor;
            if (onlineWithCard != null)
            {
                Console.WriteLine("\nДополнительно: проверка карты для онлайн-заказа:");
                onlineWithCard.ValidateCardInfo(new CardInfo());
            }

            // --------------------------------------------------------------------
            // 2. Работа с заказом с оплатой при доставке
            // --------------------------------------------------------------------
            Console.WriteLine("\n--- 2. Заказ с оплатой при доставке (наложенный платёж) ---");
            IOrderProcessor cashOrder = new CashOnDeliveryOrderProcessor();

            cashOrder.ValidateShippingAddress(new Address());
            cashOrder.ProcessOrder(new Order());

            // !!! ВНИМАНИЕ !!!
            // У объекта cashOrder нет метода ValidateCardInfo, и это правильно,
            // потому что для данного типа оплаты проверка карты не требуется.
            // Если бы мы использовали один "толстый" интерфейс, нам пришлось бы
            // реализовывать ненужный метод (например, бросать NotImplementedException),
            // что нарушило бы ISP.
            Console.WriteLine("\n  [COD] Проверка карты не требуется – метод отсутствует, и это корректно.");

            // --------------------------------------------------------------------
            // 3. Демонстрация нарушения ISP (закомментировано)
            // --------------------------------------------------------------------
            /*
            // Если бы существовал единый интерфейс IAllInOneOrderProcessor с методами
            // ValidateShippingAddress, ProcessOrder и ValidateCardInfo, то класс
            // CashOnDeliveryOrderProcessor был бы вынужден реализовать ValidateCardInfo,
            // например, так:
            // public bool ValidateCardInfo(CardInfo card) 
            // {
            //     throw new NotImplementedException("Наложенный платёж не использует карты");
            // }
            // Это привело бы к тому, что клиент, работающий с CashOnDeliveryOrderProcessor,
            // всё равно "видел" бы метод ValidateCardInfo, хотя он ему не нужен.
            // Разделение интерфейсов избавляет от этой проблемы.
            */

            Console.WriteLine("\nНажмите любую клавишу для завершения...");
            Console.ReadKey();
        }
    }
}