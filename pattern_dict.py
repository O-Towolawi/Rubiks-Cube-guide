from menu import Menu
from menu_option import MenuOption


class PatternDict(MenuOption):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: "Quit",
        }
        self.menu_text = "Coming soon... :)"

    def select_option(self, option: int):
        match option:
            case 1:
                print("Returning to main menu.")
                self.menu.trigger_menu()
            case _:
                print("Invalid option.")
                self.trigger_menu()
