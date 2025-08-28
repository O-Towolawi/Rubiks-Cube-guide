from abstract_menu import AbstractMenu
from menu_controller import MenuController
from notations import Notations


class Scrambler(AbstractMenu):
    def __init__(self):
        super().__init__()
        self.choices = {
            1: "2x2",
            2: "3x3",
            3: "4x4",
            4: "Quit",
        }
        self.menu_text = "\nWelcome to the Scrambler! Choose your cube size:"
        self.controller = MenuController()
        self.notations = Notations()

    def select_option(self, option: int):
        match option:
            case 1:
                slen = int(input("Scramble length: "))
                print(self.gen_scramble(2, slen))
            case 2:
                slen = int(input("Scramble length: "))
                print(self.gen_scramble(3, slen))
            case 3:
                slen = int(input("Scramble length: "))
                print(self.gen_scramble(4, slen))
            case 4:
                print("Returning to main scrambler menu.")
                self.controller.go_to_scrambler_menu()
            case _:
                print("Invalid option.")
                self.run()

        input("\n Press ENTER to return to scrambler menu.")
        self.controller.go_to_scrambler_menu()

    def gen_scramble(self, csize, slen):
        self.csize = csize
        self.slen = slen
        scramble = []

        print(f"\n{str(csize)}x{str(csize)} Scramble - {str(slen)} steps")

        for i in range(slen):
            next_move = self.notations.valid_moves[csize].generate_valid_move()
            scramble.append(next_move)

            # Don't repeat moves consecutively
            if i>0 and scramble[i-1][0] == scramble[i][0]:
                while scramble[i-1][0] == scramble[i][0]:
                    scramble[i] = self.notations.valid_moves[csize].generate_valid_move()

        return " ".join(scramble)