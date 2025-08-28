from abstract_menu import AbstractMenu
from menu_controller import MenuController
from notations import Notations


class X2Patterns(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: "Checkerboard",
            2: "4 columns",
            3: "Cube in a Cube",
            4: "Anaconda",
            5: "Quit",
        }
        self.menu_text = "\nWelcome to the Patterns! Choose your cube size:"
        self.controller = MenuController()
        self.notations = Notations()

    def select_option(self, option: int):
        match option:
            case 1:
                print("U R F2 U R F2 R U F' R")
            case 2:
                print("U F2 U2 R2 U")
            case 3:
                print("R F U' R2 U F' R U F2 R2")
            case 4:
                print("U R F2 U R F2 R U F' R then rotate")
                self.controller.go_to_patterns_menu()
            case _:
                print("Invalid option.")
                self.run()

        input("\n Press ENTER to return to patterns menu.")
        self.controller.go_to_patterns_menu()
