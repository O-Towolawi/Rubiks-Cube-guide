from abc import ABC, abstractmethod


class AbstractMenu(ABC):
    def __init__(self):
        self.menu_text = ""
        self.choices = {}

    def run(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            if isinstance(value, tuple):
                print(f"{key}. {value[0]}")
            else:
                print(f"{key}. {value}")
        try:
            option = int(input(f"How can we help you today [1-{len(self.choices)}]? \n"))
        except ValueError:
            print(f"Invalid option. Please choose an integer number in the range 1-{len(self.choices)}.\n")
            return self.run()
        return self.select_option(option)

    @abstractmethod
    def select_option(self, option: int):
        pass
