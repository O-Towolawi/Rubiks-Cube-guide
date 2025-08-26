class NotationsDictionary:
    def not_dict(self): #notation dictionary
        notation = {"L": "downwards", "R": "upwards", "U": "towards your left hand", "D": "towards your right hand",
                    "F": "clockwise", "B": "anti-clockwise", "M": "downwards", "x": "away from you",
                    "l": "inner left column (second from the right). Moves downwards",
                    "r": "inner right column (third from the right). Moves upwards",
                    "u": "inner upper row (second from the top). Moves towards your left hand",
                    "d": "inner bottom row (third from the top). Moves towards your right hand",
                    "f": "second from the front. Moves clockwise.", "b": "third from the front. Moves anti-clockwise."}
        special_notation = {"'": "(i.e. R') moves in opposite direction to usual. E.g. R' moves downwards",
                            "w": "(i.e. Rw) moves itself and it's lowercase notation. E.g. Rw means moving R and r (same as saying Rr, often called R sqaured)",
                            "2": "(i.e. R2) Repeat the notation twice. E.g. R2 means move the rightmost column upwards twice consecutively."}

        csize = int(input("Enter cube size [1-4]: ")) #cube size
          cs = str(csize)
          if csize > 4 or csize <1:
            while csize > 4 or csize < 1:
              print("Invalid size. Try again.")
              csize = int(input("Enter cube size [1-4]: ")) #cube size
              cs = str(csize)
          print("-"*16+cs+"x"+cs+"x"+cs+" and higher"+"-"*16)
          for move in moves[csize]:
            print("{}: {}".format(move, notation[move]))
          for symbol in special_notation:
             print("{}: {}".format(symbol, special_notation[symbol]))
          print()
          other = input("Aizes available currently are 1-4. View other cube size (y/n)? ")
          if other == "y" or other == "yes":
            print()
            not_dict()
          else:
            leave = input("Return to menu (y/n)? ")
            while leave != "y" and leave != "yes":
              leave = input("Return to menu (y/n)? ")
            print()
            print("Returning to menu...")
            print()
            menu()