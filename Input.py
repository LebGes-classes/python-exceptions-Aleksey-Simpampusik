from InputCheck import (
    InputCheckMethods,
)
from InputExceptions import (
    InputNameException, InputNumberException,
)


class InputClass:
    """Класс для входных данных."""

    @staticmethod
    def name_input() -> str:
        """Метод ввода нового имени товара, с учетом всех проверок.

        Returns:
            Новое имя.

        """

        name_input_flag = True

        new_name = None

        while name_input_flag:
            new_name = input("\nВведите название товра: ")

            try:
                new_name = InputCheckMethods.name_input_exception(new_name)

                name_input_flag = False
            except InputNameException as e:
                print(e)
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_name

    @staticmethod
    def supplier_input() -> str:
        """Метод ввода нового поставщика товара, с учетом всех проверок.

        Returns:
            Новый поставщик.

        """

        supplier_input_flag = True

        new_supplier = None

        while supplier_input_flag:
            new_supplier = input("\nВведите название поставщика: ")

            try:
                new_supplier = InputCheckMethods.name_input_exception(new_supplier)

                supplier_input_flag = False
            except InputNameException as e:
                print(e)
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_supplier

    @staticmethod
    def manufacturer_input() -> str:
        """Метод ввода нового производидтеля товара, с учетом всех проверок.

        Returns:
            Новый производитель.

        """

        manufacturer_input_flag = True

        new_manufacturer = None

        while manufacturer_input_flag:
            new_manufacturer = input("\nВведите название производителя: ")

            try:
                new_manufacturer = InputCheckMethods.name_input_exception(new_manufacturer)

                manufacturer_input_flag = False
            except InputNameException as e:
                print(e)
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_manufacturer

    @staticmethod
    def manufacturer_country_input() -> str:
        """Метод ввода новый страны производидтеля товара, с учетом всех проверок.

        Returns:
            Новая страна производителя.

        """

        manufacturer_country_input_flag = True

        new_manufacturer_country = None

        while manufacturer_country_input_flag:
            new_manufacturer_country = input("\nВведите название страны производителя: ")

            try:
                new_manufacturer_country = InputCheckMethods.name_input_exception(new_manufacturer_country)

                manufacturer_country_input_flag = False
            except InputNameException as e:
                print(e)
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_manufacturer_country

    @staticmethod
    def storage_place_input() -> str:
        """Метод ввода нового места хранения товара, с учетом всех проверок.

        Returns:
            Новое место хранения.

        """

        storage_place_input_flag = True

        new_storage_place = None

        while storage_place_input_flag:
            new_storage_place = input("\nВведите место хранения товара: ")

            try:
                new_storage_place = InputCheckMethods.name_input_exception(new_storage_place)

                storage_place_input_flag = False
            except InputNameException as e:
                print(e)
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_storage_place

    @staticmethod
    def number_of_products_input() -> int:
        """Метод ввода нового количества товаров товара, с учетом всех проверок.

        Returns:
            Новое количество товаров.

        """

        number_of_products_input_flag = True

        new_number_of_products = None

        while number_of_products_input_flag:
            try:
                new_number_of_products = int(input("\nВведите новое количество товаров: "))

                try:
                    new_number_of_products = InputCheckMethods.number_int_input_exception(new_number_of_products)

                    number_of_products_input_flag = False
                except InputNumberException as e:
                    print(e)
                except Exception as e:
                    print(f"\nПроизошла непредвиденная ошибка: {e}")
            except ValueError:
                print("\nВводимое значение может быть толко числом")
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_number_of_products

    @staticmethod
    def price_input() -> float:
        """Метод ввода новогй цены товара, с учетом всех проверок.

        Returns:
            Новая цена.

        """

        price_input_flag = True

        new_price = None

        while price_input_flag:
            try:
                new_price = float(input("\nВведите новую цену товаров: "))

                try:
                    new_price = InputCheckMethods.number_float_input_exception(new_price)

                    price_input_flag = False
                except InputNumberException as e:
                    print(e)
                except Exception as e:
                    print(f"\nПроизошла непредвиденная ошибка: {e}")
            except ValueError:
                print("\nВводимое значение может быть толко числом")
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_price

    @staticmethod
    def size_input() -> int:
        """Метод ввода нового размера товара, с учетом всех проверок.

        Returns:
            Новый рамзер.

        """

        size_input_flag = True

        new_size = None

        while size_input_flag:
            try:
                new_size = int(input("\nВведите новый размер товаров: "))

                try:
                    new_size= InputCheckMethods.number_int_input_exception(new_size)

                    size_input_flag = False
                except InputNumberException as e:
                    print(e)
                except Exception as e:
                    print(f"\nПроизошла непредвиденная ошибка: {e}")
            except ValueError:
                print("\nВводимое значение может быть толко числом")
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_size

    @staticmethod
    def weight_input() -> float:
        """Метод ввода нового веса товара, с учетом всех проверок.

        Returns:
            Новый вес товара.

        """

        weight_input_flag = True

        new_weight = None

        while weight_input_flag:
            try:
                new_weight = int(input("\nВведите новый вес товаров: "))

                try:
                    new_weight = InputCheckMethods.number_float_input_exception(new_weight)

                    weight_input_flag = False
                except InputNumberException as e:
                    print(e)
                except Exception as e:
                    print(f"\nПроизошла непредвиденная ошибка: {e}")
            except ValueError:
                print("\nВводимое значение может быть толко числом")
            except Exception as e:
                print(f"\nПроизошла непредвиденная ошибка: {e}")

        return new_weight

    @staticmethod
    def description_input() -> str:
        """Метод ввода нового описания товара, с учетом всех проверок.

        Returns:
            Новое описание товара.

        """

        description_input_flag = True

        new_description = None

        while description_input_flag:
            try:
                new_description = input("Введите новое описание товара: ")

                description_input_flag = False
            except Exception as e:
                print(f"Произошла непридвиденная ошибка: {e}")

        return new_description


