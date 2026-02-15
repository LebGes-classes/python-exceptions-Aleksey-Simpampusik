class Card:
    """Класс карточки товара."""

    def __init__ (self, name, number_of_products, supplier, manufacturer, price, _place, quality, delivery_status, description, size):
        """Конструктор класса.

        Args:
            name: имя карточки.
            number_of_products: количество товаров.
            supplier: поставщик.
            manufacturer: производитель.
            price: цена товара.
            place: место хранения.
            quality: качество товара.
            delivery_status: статус доставки товара.
            description: описание товара.
            size: размер товара.

        """

        self.name = name
        self.number_of_products = number_of_products
        self.supplier = supplier
        self.manufacturer = manufacturer
        self.price = price
        self.place = place
        self.quality = quality
        self.delivery_status = delivery_status
        self.description = description
        self.size = size

    def get_name(self):
        """Геттер имени карточки товра.

        Returns:
            Имя карточки товара.

        """

        return self.name

    def set_name(self, name):
        """Сеттер имени карточки товара.

        Args:
            name: имя товара.

        """

        self.name = name

    def get_number_of_products(self):
        """Геттер количества товаров.

        Returns:
            Кол-во товаров.

        """

        return self.number_of_products

    def set_number_of_products(self, number_of_products):
        """Сеттер имени карточки товара.

        Args:
            number_of_products: кол-во товаров.

        """

        self.number_of_products = number_of_products

    def get_supplier(self):
        """Геттер поставщика.

        Returns:
            Поставщик.

        """

        return self.name

    def set_supplier(self, supplier):
        """Сеттер поставщика.

        Args:
            supplier: поставщик.

        """

        self.supplier = supplier

    def