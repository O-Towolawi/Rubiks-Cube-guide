from abstract_menu import AbstractMenu
from menu_controller import MenuController


class PatternsMenu(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.controller = MenuController()
        self.choices = {
            1: "2x2",
            2: "3x3",
            3: "4x4",
            4: "Quit",
        }
        self.menu_text = "\nWelcome to the Patterns Menu! Choose your cube size:"

    def select_option(self, option: int):
        match option:
            case 1:
                print(self.controller.go_to_x2_patterns())
            case 2:
                print(self.controller.go_to_x3_patterns())
            case 3:
                print(self.controller.go_to_x4_patterns())
            case 4:
                print("Returning to main menu.")
                self.controller.go_to_main_menu()
            case _:
                print("Invalid option.")
                self.run()

        input("\n Press ENTER to return to scrambler menu.")
        self.controller.go_to_scrambler_menu()
