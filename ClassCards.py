class Card:
    """Класс карточки товара."""

    __delivery_requests = 0

    __registration_status = "Принято к учету"

    def __init__ (self, name: str, description: str, number_of_products: int, price: float, supplier: str, manufacturer: str, manufacturer_country: str, size: float, storage_place: str, weight: float) -> None:
        """Конструктор класса.

        Args:
            name: имя карточки.
            description: описание товара.
            number_of_products: количество товаров.
            price: цена товара.
            supplier: поставщик.
            manufacturer: производитель.
            manufacturer_country: страна производителя.
            size: размер товара.
            storage_place: место хранения.
            weight: вес товара.

        """

        self.__name = name
        self.__description = description
        self.__number_of_products = number_of_products
        self.__price = price
        self.__supplier = supplier
        self.__manufacturer = manufacturer
        self.__manufacturer_country = manufacturer_country
        self.__storage_place = storage_place
        self.__size = size
        self.__weight = weight

    def get_name(self) -> str:
        """Геттер имени карточки товра.

        Returns:
            Имя карточки товара.

        """

        return self.__name

    def set_name(self, name: str) -> None:
        """Сеттер имени товара.

        Args:
            name: имя товара.

        """

        self.__name = name

    def get_description(self) -> str:
        """Геттер описания товара.

        Returns:
            Описание товара.

        """

        return self.__description

    def set_description(self, description: str) -> None:
        """Геттер описания товара.

        Returns:
            Описание товара.

        """

        self.__description = description

    def get_number_of_products(self) -> int:
        """Геттер количества товаров.

        Returns:
            Кол-во товаров.

        """

        return self.__number_of_products

    def set_number_of_products(self, number_of_products: int) -> None:
        """Сеттер количества товара.

        Args:
            number_of_products: кол-во товаров.

        """

        self.__number_of_products = number_of_products

    def get_price(self) -> float:
        """Геттер цены товара.

        Returns:
            Цену товара.

        """

        return self.__price

    def set_price(self, price: float) -> None:
        """Сеттер цены товара.

        Args:
            price: цена товара.

        """

        self.__price = price

    def get_supplier(self) -> str:
        """Геттер поставщика.

        Returns:
            Поставщик.

        """

        return self.__supplier

    def set_supplier(self, supplier: str) -> None:
        """Сеттер поставщика.

        Args:
            supplier: поставщик.

        """

        self.__supplier = supplier

    def get_manufacturer(self) -> str:
        """Геттер проивзводителя.

        Returns:
            Название производителя.

        """

        return self.__manufacturer

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер производителя.

        Args:
            manufacturer: производидель.

        """

        self.__manufacturer = manufacturer

    def get_manufacturer_country(self) -> str:
        """Геттер страны проивзводителя.

        Returns:
            Название страны производителя.

        """

        return self.__manufacturer_country

    def set_manufacturer_country(self, manufacturer_country: str) -> None:
        """Сеттер страны производителя.

        Args:
            manufacturer_country: страна производиделя.

        """

        self.__manufacturer_country = manufacturer_country

    def get_size(self) -> float:
        """Геттер размера товара.

        Returns:
            Размер товара.

        """

        return self.__size

    def set_size(self, size: float) -> None:
        """Сеттер размера товара.

        Args:
            size: размер товаров.

        """

        self.__size = size

    def get_storage_place(self) -> str:
        """Геттер места хранения товра.

        Returns:
            Место хранения товара.

        """

        return self.__storage_place

    def set_storage_place(self, storage_place: str) -> None:
        """Сеттер места хранения товара.

        Args:
            storage_place: место хранения товара.

        """

        self.__storage_place = storage_place

    def get_weight(self) -> float:
        """Геттер веса товара.

        Returns:
            Вес товара.

        """

        return self.__weight

    def set_weight(self, weight: float) -> None:
        """Сеттер веса товара.

        Args:
            weight: вес товаров.

        """

        self.__weight = weight

    def get_delivery_requests(self) -> int:
        """Геттер количества запросов на доставку товара.

        Returns:
            Количество запросов на доставку товара.

        """

        return self.__delivery_requests

    def get_registration_status(self) -> str:
        """Геттер статуса регистрации карточки товара.

        Returns:
            Статус регистрации товара.

        """

        return self.__registration_status

    def print_info(self) -> None:
        """Выводит все атрибуты объекта класса в командную строку."""

        print(
            f"\nИмя товара: {self.get_name()}\n"
            f"Описание товара: {self.get_description()}\n"
            f"Статус регистрации карточки товара: {self.get_registration_status()}\n"
            f"Количество продуктов: {self.get_number_of_products()}\n"
            f"Цена товара: {self.get_price()}\n"
            f"Поставщик товара: {self.get_supplier()}\n"
            f"Производитель товара: {self.get_manufacturer()}\n"
            f"Страна производителя товара: {self.get_manufacturer_country()}\n"
            f"Размер товара: {self.get_size()}\n"
            f"Место хранения товара: {self.get_storage_place()}\n"
            f"Вес товара: {self.get_weight()}\n"
            f"Количество запросов на доставку товара: {self.get_delivery_requests()}\n"
        )

    def confirm_card(self) -> None:
        """Принятие товара на учет."""

        if self.__registration_status == "Снято с учета":
            print("Товар снят с учета.")
        elif self.__registration_status == "Стоит на учете":
            print("Товар уже стоит на учете.")
        else:
            self.__registration_status = "Стоит на учете"

            print("Товар поставлен на учёт.")

    def discard_card(self) -> None:
        """Снятие товара с учета."""

        if self.__registration_status == "Снято с учета":
            print("Товар уже снят с учета.")
        else:
            self.__registration_status = "Снято с учета"

            print("Товар снят с учёта.")

    def request_delivery(self) -> None:
        """Увеличивает количество заказов на доставку товара."""

        if self.__registration_status == "Стоит на учете":
            if self.__number_of_products > 0:
                self.__number_of_products -= 1
                self.__delivery_requests += 1
            else:
                print("На складе нет товаров.")
        else:
            print("Товар не стоит на учете или еще не принят к учету.")

    def cancel_delivery(self) -> None:
        """Отменяет доставку и возвращает товар на склад."""

        if self.__registration_status == "Стоит на учете":
            if self.__delivery_requests > 0:
                self.__number_of_products += 1
                self.__delivery_requests -= 1

                print("Доставка отменена.")
            else:
                print("Невозможно отменить достаку: нет запросов.")
        else:
            print("Товар не стоит на учете или еще не принят к учету.")

    def end_delivery(self) -> None:
        """Завершает доставку."""

        if self.__registration_status == "Стоит на учете":
            if self.__delivery_requests > 0:
                self.__delivery_requests -= 1

                print("Доставка завершена.")
            else:
                print("Невозможно завершить достаку: нет запросов.")
        else:
            print("Товар не стоит на учете или еще не принят к учету.")

