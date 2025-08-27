from abstract_menu_option import MenuOption


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

        self._x2_notations_set = {"L", "R", "U", "D", "F", "B", "x"}
        self._x3_notations_set = self._x2_notations_set | {"M"}
        self._x4_notations_set = self.notations_dict.keys()

        # special notations
        self.direction_notations = {
            "'": "moves in opposite direction to usual",
            "w": "(i.e. Rw) moves itself and it's lowercase notation. E.g. Rw means moving R and r (same as saying Rr, often called R sqaured)",
        }
        self.move_count_notations = {
            "2": "(i.e. R2) Repeat the notation twice. E.g. R2 means move the rightmost column upwards twice consecutively."
        }

    def select_option(self, option: int):
        print(self.direction_notations)
        print(self.move_count_notations)
        match option:
            case 1:
                print(self.get_x2_notations())
            case 2:
                print(self.get_x3_notations())
            case 3:
                print(self.get_x4_notations())
            case 4:
                leave = input("Return to menu (y/n)? ")
                match leave:
                    case "y" | "yes":
                        print("Returning to main menu.")
                        self.menu.run()
                    case "n" | "no":
                        self.run()
                    case _:
                        print("Invalid option.")
                        self.run()

            case _:
                print("Invalid option.")
                self.run()

    def get_x2_notations(self):  # 2x2 or higher
        return {
            k: v for k, v in self.notations_dict.items() if k in self._x2_notations_set
        }

    def get_x3_notations(self):  # 3x3 or higher
        return {
            k: v for k, v in self.notations_dict.items() if k in self._x3_notations_set
        }

    def get_x4_notations(self):  # 4x4 or higher
        return self.notations_dict

    def get_all_notations(self):
        return self.notations_dict