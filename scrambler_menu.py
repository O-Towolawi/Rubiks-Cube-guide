from menu import Menu
from scrambler import Scrambler


class ScramblerMenu:
    def __init__(self):
        self.menu = Menu()
        self.choices = {
            1: "Generate a scramble",
            2: "Quit",
        }
        self.menu_text = "Coming soon... Returning to menu :)"

    def trigger_menu(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            print(f"{key}. {value}")
        option = int(input("How can we help you today [1-4]? "))

        return option

    def select_option(self, option: int):
        match option:
            case 1:
                self.scrambler = Scrambler()
                self.scrambler.trigger_menu()
            case 2:
                print("Returning to main menu.")
                self.menu.trigger_menu()