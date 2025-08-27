from abstract_menu_option import MenuOption
from concrete_commands import OpenNotationsDictionaryCommand, OpenScramblerCommand, OpenPatternDictCommand, \
    CloseMainMenuCommand, ReturnToMainMenuCommand
from notations_dictionary import NotationsDictionary


class MainMenu(MenuOption):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: ["Notations dictionary", NotationsDictionary],
            2: ["Scrambler", Scrambler],
            3: ["Patterns dictionary", PatternDict],
            4: ["Quit", self.close]
        }
        self.menu_text = "Welcome to the Rubik's Cube help desk! Here are your options:"

    def run(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            print(f"{key}. {value[0]}")
        option = int(input(f"How can we help you today [1-{len(self.choices)}]? "))
        return option

    def select_option(self, menu_option):
        try:
            menu_option.run()
        except KeyError:
            print("Invalid option.")
            return ReturnToMainMenuCommand().execute()
        except IndexError:
            print(f"Invalid option. Please choose an integer number in the range 1-{len(self.choices)}.")
            return ReturnToMainMenuCommand().execute()


    def close(self):
        print("Thank you for using the Rubik's Cube help desk.")
        input("Press ENTER to quit.")
