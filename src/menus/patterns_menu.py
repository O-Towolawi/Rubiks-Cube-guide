from src.menus.abstract_menu import AbstractMenu
from src.utils.menu_controller import MenuController


class PatternsMenu(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.controller = MenuController()
        self.choices = {
            1: "Quit",
        }
        self.menu_text = "Coming soon... :)"

    def select_option(self, option: int):
        match option:
            case 1:
                print("Returning to main menu.")
                self.controller.go_to_main_menu()
            case _:
                print("Invalid option.")
                self.run()
