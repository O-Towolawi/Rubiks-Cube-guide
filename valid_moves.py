import random

from abstract_valid_move import AbstractValidMoves


class X2ValidMoves(AbstractValidMoves):
    def __init__(self):
        super().__init__()

    def get_valid_moves(self):
        return "L", "R", "U", "D", "F", "B", "x"

    def get_valid_directions(self):
        return "", "'"

    def get_valid_counts(self):
        return "", "2"


class X3ValidMoves(AbstractValidMoves):
    def __init__(self):
        super().__init__()

    def get_valid_moves(self):
        return X2ValidMoves().get_valid_moves() + ("M",)

    def get_valid_directions(self):
        return X2ValidMoves().get_valid_directions() + ("w",)

    def get_valid_counts(self):
        return X2ValidMoves().get_valid_counts()

    def generate_valid_move(self):
        random_move = random.choice(self.get_valid_moves())
        random_direction = random.choice(self.get_valid_directions())
        random_count = random.choice(self.get_valid_counts())

        # Reroll invalid moves
        if random_move == "M" and random_direction == "w":
            return self.generate_valid_move()

        return random_move + random_direction + random_count


class X4ValidMoves(AbstractValidMoves):
    def __init__(self):
        super().__init__()

    def get_valid_moves(self):
        return X3ValidMoves().get_valid_moves() + ("l", "r", "u", "d", "f", "b")

    def get_valid_directions(self):
        return X3ValidMoves().get_valid_directions()

    def get_valid_counts(self):
        return X3ValidMoves().get_valid_counts()

    def generate_valid_move(self):
        random_move = random.choice(self.get_valid_moves())
        random_direction = random.choice(self.get_valid_directions())
        random_count = random.choice(self.get_valid_counts())

        # Reroll invalid moves
        if random_move in self.invalid_wide_notations:
            return self.generate_valid_move()

        return random_move + random_direction + random_count
