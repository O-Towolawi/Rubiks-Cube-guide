from abstract_menu_option import MenuOption
from concrete_commands import OpenNotationsDictionaryCommand, OpenScramblerCommand, OpenPatternDictCommand, \
    CloseMainMenuCommand, ReturnToMainMenuCommand


class MainMenu(MenuOption):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: ["Notations dictionary", OpenNotationsDictionaryCommand()],
            2: ["Scrambler", OpenScramblerCommand()],
            3: ["Patterns dictionary", OpenPatternDictCommand()],
            4: ["Quit", CloseMainMenuCommand()]
        }
        self.menu_text = "Welcome to the Rubik's Cube help desk! Here are your options:"

    def select_option(self):
        option = self.run()
        try:
            self.choices[option][1].execute()
        except KeyError:
            print("Invalid option.")
            return ReturnToMainMenuCommand().execute()
        except IndexError:
            print(f"Invalid option. Please choose an integer number in the range 1-{len(self.choices)}.")
            return ReturnToMainMenuCommand().execute()


    def close(self):
        print("Thank you for using the Rubik's Cube help desk.")
        input("Press ENTER to quit.")
