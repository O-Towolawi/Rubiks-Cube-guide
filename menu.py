from notations_dictionary import NotationsDictionary
from pattern_dict import PatternDict
from scrambler import Scrambler


class Menu:
    def __init__(self):
        self.options = [
            "Notations dictionary",
            "Scrambler",
            "Patterns dictionary",
            "Quit",
        ]
        self.choices = {
            1: "Notations dictionary",
            2: "Scrambler",
            3: "Patterns dictionary",
            4: "Quit",
        }
        self.menu_text = "Welcome to the Rubik's Cube help desk! Here are your options:"

    def trigger_menu(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            print(f"{key}. {value}")
        option = int(input("How can we help you today [1-4]? "))

        return option

    def select_option(self, option: int):
        match option:
            case 1:
                NotationsDictionary().trigger_menu()
            case 2:
                Scrambler().trigger_menu()
            case 3:
                PatternDict().trigger_menu()
            case 4:
                self.close()
            case _:
                print("Invalid option. Returning to menu...")
                self.trigger_menu()


    def close(self):
        print("Thank you for using the Rubik's Cube help desk.")
        input("Press ENTER to quit.")
