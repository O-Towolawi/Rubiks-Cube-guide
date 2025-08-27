from abc import ABC, abstractmethod
from menu import Menu


class MenuOption(ABC):
    def __init__(self):
        self.menu = Menu()
        self.menu_text = ""
        self.choices = {}

    def trigger_menu(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            print(f"{key}. {value}")
        option = int(input(f"How can we help you today [1-{len(self.choices)}]? "))
        return option

    @abstractmethod
    def select_option(self, option: int):
        pass
