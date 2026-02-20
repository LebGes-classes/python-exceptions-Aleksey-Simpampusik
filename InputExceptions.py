class InputNameException(Exception):
    """Класс ошибки имени."""

    def __init__(self, message = "\nНевозможное для введения имя.") -> None:
        """Конструктор класса."""

        self.__message = message

    def __str__(self) -> str:
        """Выводит сообщение об ошибке"""

        return self.__message

class InputNumberException(Exception):
    """Класс ошибки чисел."""

    def __init__(self, message="\nНевозможное для записи число.") -> None:
        """Конструктор класса."""

        self.__message = message

    def __str__(self) -> str:
        """Выводит сообщение об ошибке"""

        return self.__message



