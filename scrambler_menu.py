from abstract_menu import AbstractMenu
from menu_controller import MenuController


class ScramblerAbstractMenu(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: "Generate a scramble",
            2: "Quit",
        }
        self.menu_text = "Welcome to the Scrambler! Please choose an option:"
        self.controller = MenuController()

    def select_option(self, option: int):
        match option:
            case 1:
                self.controller.go_to_scrambler()
            case 2:
                print("Returning to main menu.")
                self.controller.go_to_main_menu()
