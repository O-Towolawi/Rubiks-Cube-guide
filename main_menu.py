from abstract_menu import AbstractMenu
from menu_controller import MenuController


class MainMenu(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.controller = MenuController()
        self.choices = {
            1: ("Notations dictionary", self.controller.go_to_notations_menu),
            2: ("Scrambler", self.controller.go_to_scrambler_menu),
            3: ("Patterns dictionary", self.controller.go_to_patterns_menu),
            4: ("Quit", self.close)
        }
        self.menu_text = "Welcome to the Rubik's Cube help desk!\nHere are your options:"


    def select_option(self, menu_option):
        try:
            option = self.choices[menu_option][1]
            return option()
            
        except KeyError:
            print(f"Invalid option. Please choose an integer number in the range 1-{len(self.choices)}.\n")
            return self.controller.go_to_main_menu()
        except IndexError:
            print(f"Invalid option. Please choose an integer number in the range 1-{len(self.choices)}.\n")
            return self.controller.go_to_main_menu()


    def close(self):
        print("Thank you for using the Rubik's Cube help desk.")
        input("Press ENTER to quit.")
        exit(0)
