import random

from menu import Menu
from notations_dictionary import NotationsDictionary
from scrambler_menu import ScramblerMenu


class Scrambler:
    def __init__(self):
        self.menu = Menu()
        self.choices = {
            1: "2x2",
            2: "3x3",
            3: "4x4",
            4: "Quit",
        }
        self.menu_text = "Welcome to the Scrambler! Choose your cube size:"

        # all notation and combintations depending on cube size
        self.notations = NotationsDictionary.get_notations(NotationsDictionary())
        self.mdir = self.notations["directions_notations"]  # move direction
        self.mcount = self.notations["move_count_notations"]  # move count
        self.moves = self.notations["notations_list"]

    def trigger_menu(self) -> int:
        print(self.menu_text)
        for key, value in self.choices.items():
            print(f"{key}. {value}")
        option = int(input("How can we help you today [1-4]? "))

        return option

    def select_option(self, option: int):
        slen = int(input("Scramble length: "))
        match option:
            case 1:
                self.gen_scramble(2, slen)
            case 2:
                self.gen_scramble(3, slen)
            case 3:
                self.gen_scramble(4, slen)
            case 4:
                print("Returning to menu.")
                self.trigger_menu()
            case _:
                print("Invalid option. Returning to menu...")
                self.trigger_menu()

    def gen_scramble(self, csize, slen):
        self.csize = csize
        self.slen = slen

        print(
            (str(csize) + "x") * 2
            + str(csize)
            + " Scramble"
            + " - "
            + str(slen)
            + " steps"
        )
        s = self.valid(
            [
                [
                    random.choice(self.moves[csize]),
                    random.choice(self.mdir),
                    random.choice(self.mcount),
                ]
                for i in range(slen)
            ],
            csize,
        )
        return "".join(s[x][0] + s[x][1] + s[x][2] + " " for x in range(len(s)))

    def valid(self, ar, csize):
        for x in range(len(ar)):
            if ar[x][0] in self.moves[csize][-7:-1]:
                ar[x][1] = random.choice(self.mdir[:2])
        for x in range(1, len(ar)):
            while ar[x][0] == ar[x - 1][0]:
                ar[x][0] = random.choice(self.moves[csize])
        for x in range(2, len(ar)):
            while ar[x][0] == ar[x - 2][0] or ar[x][0] == ar[x - 1][0]:
                ar[x][0] = random.choice(self.moves[csize])
        return ar
