from abstract_menu import AbstractMenu
from menu_controller import MenuController
from notations import Notations


class NotationsMenu(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: "2x2",
            2: "3x3",
            3: "4x4",
            4: "Quit",
        }
        self.menu_text = "Welcome to the Notations guide!\nHere are your options:"
        self.controller = MenuController()
        self.notations = Notations()

    def select_option(self, option: int):
        if option != 4:
            self.notations.get_special_notations()

        match option:
            case 1:
                print("2x2 or higher:")
                print(self.notations.get_x2_notations(), "\n")

                input("Press ANY KEY to return to menu.")
                self.controller.go_to_notations_menu()
            case 2:
                print("3x3 or higher:")
                print(self.notations.get_x3_notations(), "\n")

                input("Press ANY KEY to return to menu.")
                self.controller.go_to_notations_menu()
            case 3:
                print("4x4or higher:")
                print(self.notations.get_x4_notations(), "\n")

                input("Press ANY KEY to return to menu.")
                self.controller.go_to_notations_menu()
            case 4:
                leave = input("Return to menu (y/n)? ")
                match leave:
                    case "y" | "yes":
                        print("Returning to main menu.", "\n")
                        self.controller.go_to_main_menu()
                    case "n" | "no":
                        self.run()
                    case _:
                        print("Invalid option.", "\n")
                        self.run()

            case _:
                print("Invalid option.")
                self.run()
