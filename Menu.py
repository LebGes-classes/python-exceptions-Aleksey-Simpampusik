from ClassCards import (
    Card,
)
from Input import (
    InputClass as Input,
)


class Menu:
    """Класс меню."""

    @staticmethod
    def print_commands() -> None:
        """Выводит список комманд для взаимодействия с классом."""

        print("\n0 - Выход из программы\n"
              "1 - Узнать характеристики товара\n"
              "2 - Принять товар на учет\n"
              "3 - Снять товар с учета\n"
              "4 - Заказать доставку товара\n"
              "5 - Отменить доставку товара\n"
              "6 - Завершить доставку товара\n"
              "7 - Поменять название товара\n"
              "8 - Поменять описание товара\n"
              "9 - Поменять количество товаров\n"
              "10 - Поменять цену товара\n"
              "11 - Поменять поставщика товара\n"
              "12 - Поменять производителя товара\n"
              "13 - Поменять страну производителя товара\n"
              "14 - Поменять размер товара\n"
              "15 - Поменять место хранения товара\n"
              "16 - Поменять вес товара\n"
        )

    def main_menu(self, choice: int, card: Card) -> bool:
        """Главное пользовательское меню.

        Args:
            choice: выбор команды пользователя.
            card: карточка товара, выбранная пользователем.

        Returns:
            is_running: продолжает ли работать программа

        """

        is_running = True

        match choice:
            case 0:
                is_running = False
            case 1:
                card.print_info()
            case 2:
                card.confirm_card()
            case 3:
                card.discard_card()
            case 4:
                card.request_delivery()
            case 5:
                card.cancel_delivery()
            case 6:
                card.end_delivery()
            case 7:
                new_name = Input.name_input()

                card.set_name(new_name)
            case 8:
                new_description = Input.description_input() #Без проверки, так как описание может быть любое.

                card.set_description(new_description)
            case 9:
                new_number_of_products = Input.number_of_products_input()

                card.set_number_of_products(new_number_of_products)
            case 10:
                new_price = Input.price_input()

                card.set_price(new_price)
            case 11:
                new_supplier = Input.supplier_input()

                card.set_supplier(new_supplier)
            case 12:
                new_manufacturer = Input.manufacturer_input()

                card.set_manufacturer(new_manufacturer)
            case 13:
                new_manufacturer_country = Input.manufacturer_country_input()

                card.set_manufacturer_country(new_manufacturer_country)
            case 14:
                new_size = Input.size_input()

                card.set_size(new_size)
            case 15:
                new_storage_place = Input.storage_place_input()

                card.set_storage_place(new_storage_place)
            case 16:
                new_weight = Input.weight_input()

                card.set_weight(new_weight)

        return is_running