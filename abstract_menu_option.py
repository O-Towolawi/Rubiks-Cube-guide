from abc import ABC, abstractmethod
from main_menu import MainMenu


class MenuOption(ABC):
    def __init__(self):
        self.menu = MainMenu()
        self.menu_text = ""
        self.choices = {}

    def run(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            print(f"{key}. {value[0]}")
        option = int(input(f"How can we help you today [1-{len(self.choices)}]? "))
        return option

    def close(self):
        pass

    @abstractmethod
    def select_option(self, option: int):
        pass
