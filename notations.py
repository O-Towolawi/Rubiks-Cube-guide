from valid_moves import X2ValidMoves, X3ValidMoves, X4ValidMoves

class Notations:
    def __init__(self):

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

        self.valid_moves = {2: X2ValidMoves(), 3: X3ValidMoves(), 4: X4ValidMoves()}

    def get_direction_notations(self):
        return {
            "'": "moves in opposite direction to usual",
            "w": "(i.e. Rw) moves itself and it's lowercase notation. E.g. Rw means moving R and r (same as saying Rr, often called R sqaured)",
        }

    def get_move_count_notations(self):
        return {
            "2": "(i.e. R2) Repeat the notation twice. E.g. R2 means move the rightmost column upwards twice consecutively."
        }

    def get_special_notations(self):
        print("\nDirectional Notations:")
        print(self.get_direction_notations(), "\n")
        print("Move Count Notations:")
        print(self.get_direction_notations(), "\n")

    def get_x2_notations(self):  # 2x2 or higher
        return {
            k: v
            for k, v in self.notations_dict.items()
            if k in X2ValidMoves().get_valid_moves()
        }

    def get_x3_notations(self):  # 3x3 or higher
        return {
            k: v
            for k, v in self.notations_dict.items()
            if k in X3ValidMoves().get_valid_moves()
        }

    def get_x4_notations(self):  # 4x4 or higher
        return {
            k: v
            for k, v in self.notations_dict.items()
            if k in X4ValidMoves().get_valid_moves()
        }

    def get_all_notations(self):
        return {
            "direction_notations": self.direction_notations,
            "move_count_notations": self.move_count_notations,
            "general_notations": self.notations_dict,
        }