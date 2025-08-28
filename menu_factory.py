from abc import ABC, abstractmethod

from concrete_commands import GoToMenuCommand
from main_menu import MainMenu


class AbstractMenu(ABC):
    def __init__(self):
        self.choices = {} # int: [description, call command]
        self.menu_text = "" # Menu description

    def run(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            print(f"{key}. {value[0]}")
        option = int(input(f"How can we help you today [1-{len(self.choices)}]? "))
        return option

    def close(self):
        print("Returning to main menu.")
        return GoToMenuCommand().execute()

    @abstractmethod
    def select_option(self, menu_option):
        try:
            menu_option.run()
        except KeyError:
            print("Invalid option.")
            return self.run()
        except IndexError:
            print(f"Invalid option. Please choose an integer number in the range 1-{len(self.choices)}.")
            return self.run()