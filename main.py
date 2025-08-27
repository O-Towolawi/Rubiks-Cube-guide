import random

# all notation and combintations depending on cube size
all_moves = ["L", "R", "U", "D", "F", "B", "M", "x", "l", "r", "u", "d", "f", "b"]
moves = {1: all_moves[:6], 2: all_moves[:6], 3: all_moves[:8], 4: all_moves}
mdir = ["", "'", "w"]  # move direction
mcount = ["", "2"]  # move count

if __name__ == "__main__":
    menu()
