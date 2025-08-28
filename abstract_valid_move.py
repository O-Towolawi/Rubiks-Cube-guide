import random
from abc import ABC, abstractmethod


class AbstractValidMoves(ABC):
    def __init__(self):
        self.invalid_wide_notations = ("x", "M", "l", "r", "u", "d", "f", "b")

    @abstractmethod
    def get_valid_moves(self):
        pass

    @abstractmethod
    def get_valid_directions(self):
        pass

    @abstractmethod
    def get_valid_counts(self):
        pass

    def generate_valid_move(self):
        random_moves = random.choice(self.get_valid_moves())
        random_direction = random.choice(self.get_valid_directions())
        random_count = random.choice(self.get_valid_counts())

        return random_moves + random_direction + random_count