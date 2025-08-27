from menu_options.notations_dictionary import *
from menu_options.scrambler import *
from menu_options.pattern_dict import *


def details():
    csize = int(input("Enter cube size [1-4]: "))  # cube size
    try:
        slen = int(input("Scramble length: "))  # length of scramble
        while slen < 1:
            print("Please enter a positive integer.")
            slen = int(input("Scramble length: "))
    except:
        print("Please enter a positive integer.")
        slen = int(input("Scramble length: "))
        while slen < 1:
            print("Please enter a positive integer.")
            slen = int(input("Scramble length: "))
    return (csize, slen)


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

    def select_option(self, option: int) -> str:
        match option:
            case 1:
                NotationsDictionary.trigger_menu()
            case 2:
                Scrambler.trigger_menu()
            case 3:
                PatternDict.trigger_menu()
            case 4:
                end()
            case _:
                print("Invalid option. Returning to menu...")
                self.trigger_menu()


def end():
    print("Thank you for using the Rubik's Cube help desk.")
    input("Press ENTER to quit.")
