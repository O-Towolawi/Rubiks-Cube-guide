from main_menu import MainMenu
from abstract_menu_option import MenuOption
from scrambler import Scrambler


class ScramblerMenu(MenuOption):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: "Generate a scramble",
            2: "Quit",
        }
        self.menu_text = "Welcome to the Scrambler! Please choose an option:"

    def select_option(self, option: int):
        match option:
            case 1:
                self.scrambler = Scrambler()
                self.scrambler.run()
            case 2:
                print("Returning to main menu.")
                self.menu.run()
