from InputExceptions import (
    InputNameException, InputNumberException
)

import re


class InputCheckMethods():
    """Класс обработки исключений ошибок для входных данных"""

    @staticmethod
    def name_input_exception(new_name: str) -> str:
        """Проверка имени на вход.

        Args:
            new_name: новое имя для обработки

        Returns:
            То же имя, если оно удовлетворяет условиям. Иначе вызвывается ошибка.

        """

        name_regular = r'\s+'

        match_new_name = re.fullmatch(name_regular, new_name)

        if new_name == "" or match_new_name is not None:
            raise InputNameException()

        while new_name[0] == " ":
            new_name = new_name[1:]

        return new_name

    @staticmethod
    def number_int_input_exception(new_number: int) -> int:
        """Проверка числа на вход.

        Args:
            new_number: число для проверки.

        Returns:
            То же число, если оно подходит по условиям.Ииначе вызывается ошибка.

        """

        if new_number < 0:
            raise InputNumberException()

        return new_number

    @staticmethod
    def number_float_input_exception(new_number: float) -> float:
        """Проверка числа на вход.

        Args:
            new_number: Новое число с плавающей запятой.

        Returns:
            То же число, если оно проходит проверки. Иначе вызывается ошибка.

        """

        if new_number < 0:
            raise InputNumberException()

        return new_number






