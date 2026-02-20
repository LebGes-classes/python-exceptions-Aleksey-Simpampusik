from ClassCards import (
    Card,
)
from Menu import (
    Menu,
)

menu = Menu()

Cards_dict = {
    "Milk": Card("Milk", "2% Fat 100 ml", 100, 120.6, "Storage Provider 12", "Prostokvashino", "Russia", 1.2, "Storage 172", 120.0),
    "Bread": Card("Bread", "Wheat bread 500g", 500, 45.5, "Storage Provider 5", "Khlebny Dom", "Russia", 0.8, "Storage 45", 45.0),
    "Eggs": Card("Eggs", "Chicken eggs 10 pcs", 10, 89.9, "Storage Provider 8", "Roskar", "Russia", 0.6, "Storage 23", 85.0)
}


def select_card() -> Card:
    """Метод для выбора карточки из словаря.

    Returns:
        Выбранная карточка.

    """

    print("\nДоступные товары:")

    for key in Cards_dict.keys():
        print(f"  - {key}")

    card_chosen_flag = False

    selected_card = None

    while not card_chosen_flag:
        try:
            choice_product = input("\nВведите название товара или 0 для выхода: ")

            if choice_product == '0':
                print("\nВыход из выбора карточки.")

                card_chosen_flag = True

            elif not choice_product:
                print("\nНазвание товара не может быть пустым.")

            elif choice_product in Cards_dict:
                selected_card = Cards_dict[choice_product]

                print(f"\nВыбрана карточка товара {choice_product}")

                card_chosen_flag = True

            else:
                print(f"\nТовар '{choice_product}' не найден в словаре")
        except Exception as e:
            print(f"\nПроизошла непредвиденная ошибка: {e}")

            card_chosen_flag = True

    return selected_card


def choose_command() -> int:
    """Метод для выбора комнады.

    Returns:
        Выбранная комнада.

    """

    menu.print_commands()

    command_chosen_flag = False

    selected_command = None

    while not command_chosen_flag:
        try:
            selected_command = int(input("\nВыберите комнаду или напишите 0 для выхода из программы: "))

            if 0<=selected_command<=16:
                command_chosen_flag = True

            elif not selected_command:
                print("\nКоманда не может быть пустой.")

            else:
                print("\nТакой команды нет.")
        except ValueError:
            print("\nКоманда может быть только числом.")
        except Exception as e:
            print(f"\nПроизошла непридвединныя ошибка: {e}")

    return selected_command

def run() -> None:
    """Метод запуска работы программы."""

    is_running = True

    while is_running:
        selected_card = None

        while selected_card is None:
            selected_card = select_card()

            if selected_card is None:
                print("\nВы не выбрали карточку товара.")

        selected_command = None

        while selected_command is None:
            selected_command = choose_command()

        try:
            is_running = menu.main_menu(selected_command, selected_card)
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


run()


