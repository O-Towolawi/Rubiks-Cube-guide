from menu import Menu


class NotationsDictionary:
    def __init__(self):
        self.notations = {}
        self.menu = Menu()

        # special notations
        self.special_notations = {"'": "(i.e. R') moves in opposite direction to usual. E.g. R' moves downwards",
                                  "w": "(i.e. Rw) moves itself and it's lowercase notation. E.g. Rw means moving R and r (same as saying Rr, often called R sqaured)",
                                  "2": "(i.e. R2) Repeat the notation twice. E.g. R2 means move the rightmost column upwards twice consecutively."}
        # 2x2 or higher
        self.basic_notations = {"L": "downwards",
                                "R": "upwards",
                                "U": "towards your left hand",
                                "D": "towards your right hand",
                                "F": "clockwise",
                                "B": "anti-clockwise",
                                "x": "away from you"}
        # 3x3 or higher
        self.intermediate_notations = {"M": "centre row towards you"}

        # 4x4 or higher
        self.advanced_notations = {"l": "inner left column (second from the right). Moves downwards",
                                   "r": "inner right column (third from the right). Moves upwards",
                                   "u": "inner upper row (second from the top). Moves towards your left hand",
                                   "d": "inner bottom row (third from the top). Moves towards your right hand",
                                   "f": "second from the front. Moves clockwise.",
                                   "b": "third from the front. Moves anti-clockwise."}

        self.notations["special_notations"] = self.special_notations
        self.notations["2x2 or higher"] = self.basic_notations
        self.notations["3x3 or higher"] = self.intermediate_notations
        self.notations["4x4 or higher"] = self.advanced_notations

        self.choices = {
            1: "2x2",
            2: "3x3",
            3: "4x4",
            4: "Quit",
        }
        self.menu_text = "Welcome to the Notations guide! Here are your options:"

    def trigger_menu(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            print(f"{key}. {value}")
        option = int(input("How can we help you today [1-4]? "))

        return option

    def select_option(self, option: int):
        print(self.notations["special_notations"])
        match option:
            case 1:
                print(self.notations["2x2 or higher"])
            case 2:
                print(self.notations["2x2 or higher"])
                print(self.notations["3x3 or higher"])
            case 3:
                print(self.notations["2x2 or higher"])
                print(self.notations["3x3 or higher"])
                print(self.notations["4x4 or higher"])
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