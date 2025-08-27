from menu import Menu
from menu_option import MenuOption


class NotationsDictionary(MenuOption):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: "2x2",
            2: "3x3",
            3: "4x4",
            4: "Quit",
        }
        self.menu_text = "Welcome to the Notations guide! Here are your options:"

        self.notations_dict = {
            "L": "downwards",
            "R": "upwards",
            "U": "towards your left hand",
            "D": "towards your right hand",
            "F": "clockwise",
            "B": "anti-clockwise",
            "x": "away from you",
            "M": "centre row towards you",
            "l": "inner left column (second from the right). Moves downwards",
            "r": "inner right column (third from the right). Moves upwards",
            "u": "inner upper row (second from the top). Moves towards your left hand",
            "d": "inner bottom row (third from the top). Moves towards your right hand",
            "f": "second from the front. Moves clockwise.",
            "b": "third from the front. Moves anti-clockwise.",
        }
        self.notations_list = self.notations_dict.keys()

        # special notations
        self.direction_notations = {
            "'": "moves in opposite direction to usual",
            "w": "(i.e. Rw) moves itself and it's lowercase notation. E.g. Rw means moving R and r (same as saying Rr, often called R sqaured)",
        }
        self.move_count_notations = {
            "2": "(i.e. R2) Repeat the notation twice. E.g. R2 means move the rightmost column upwards twice consecutively."
        }
        # 2x2 or higher
        self.x2_notations = {
            k: v for k, v in self.notations_dict.items() if k in self.notations_list[:6]
        }
        # 3x3 or higher
        self.x3_notations = {
            k: v for k, v in self.notations_dict.items() if k in self.notations_list[:7]
        }

        # 4x4 or higher
        self.x4_notations = self.notations_dict

    @staticmethod
    def get_notations():
        return {
            "notations_list": NotationsDictionary().notations_list,
            "notations_dict": NotationsDictionary().notations_dict,
            "direction_notations": NotationsDictionary().direction_notations,
            "move_count_notations": NotationsDictionary().move_count_notations,
            "2x2_notations": NotationsDictionary().x2_notations,
            "3x3_notations": NotationsDictionary().x3_notations,
            "4x4_notations": NotationsDictionary().x4_notations,
        }

    def select_option(self, option: int):
        print(self.direction_notations)
        print(self.move_count_notations)
        match option:
            case 1:
                print(self.x2_notations)
            case 2:
                print(self.x3_notations)
            case 3:
                print(self.x4_notations)
            case 4:
                leave = input("Return to menu (y/n)? ")
                match leave:
                    case "y" | "yes":
                        print("Returning to main menu.")
                        self.menu.trigger_menu()
                    case "n" | "no":
                        self.trigger_menu()
                    case _:
                        print("Invalid option.")
                        self.trigger_menu()

            case _:
                print("Invalid option.")
                self.trigger_menu()
