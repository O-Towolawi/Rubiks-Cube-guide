import random

#all notation and combintations depending on cube size
all_moves = ["L", "R", "U", "D", "F", "B", "M", "x", "l", "r", "u", "d", "f", "b"]
moves = {1: all_moves[:6], 2: all_moves[:6], 3: all_moves[:8], 4: all_moves}
mdir = ["", "'", "w"] #move direction
mcount = ["", "2"] #move count

def not_dict(): #notation dictionary
  notation = {"L": "downwards", "R": "upwards", "U": "towards your left hand", "D": "towards your right hand", "F": "clockwise", "B": "anti-clockwise", "M": "downwards", "x": "away from you", "l": "inner left column (second from the right). Moves downwards", "r": "inner right column (third from the right). Moves upwards", "u": "inner upper row (second from the top). Moves towards your left hand", "d": "inner bottom row (third from the top). Moves towards your right hand", "f": "second from the front. Moves clockwise.", "b": "third from the front. Moves anti-clockwise."}
  special_notation = {"' (i.e. R')": "moves in opposite direction to usual. E.g. R' moves downwards", "w (i.e. Rw)": "moves itself and it's lowercase notation. E.g. Rw means moving R and r (same as saying Rr, often called R sqaured)", "2 (i.e. R2)": "Repeat the notation twice. E.g. R2 means move the rightmost column upwards twice consecutively."}
  for i in range(1,5):
    j = str(i)
    print("-"*16+j+"x"+j+"x"+j+" and higher"+"-"*16)
    for move in moves[i]:
      print("{}: {}".format(move, notation[move]))
  for symbol in special_notation:
     print("{}: {}".format(symbol, special_notation[symbol]))
  print()
  leave = input("Return to menu (y/n)? ")
  while leave != "y" and leave != "yes":
     leave = input("Return to menu (y/n)? ")
  print()
  print("Returning to menu...")
  print()
  menu()

def gen_scramble():
  csize = int(input("Enter cube size [1-4]: ")) #cube size
  try:
      slen = int(input("Scramble length: ")) #length of scramble
      while slen < 1:
          print("Please enter a positive integer.")
          slen = int(input("Scramble length: "))
  except:
      print("Please enter a positive integer.")
      slen = int(input("Scramble length: "))
      while slen < 1:
          print("Please enter a positive integer.")
          slen = int(input("Scramble length: "))
  print()
  print((str(csize) + "x")*2 + str(csize) + " Scramble" + " - " + str(slen) + " steps" )
  s = valid([[random.choice(moves[csize]), random.choice(mdir), random.choice(mcount)] for i in range(slen)], csize)
  return ''.join(s[x][0] + s[x][1] + s[x][2] + " "for x in range(len(s)))

def valid(ar, csize):
  for x in range (len(ar)):
    if ar[x][0] in moves[csize][-7:-1]:
      ar[x][1] = random.choice(mdir[:2])
  for x in range(1, len(ar)):
      while ar[x][0] == ar[x-1][0]:
          ar[x][0] = random.choice(moves[csize])
  for x in range (2, len(ar)):
      while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
          ar[x][0] = random.choice(moves[csize])
  return ar

def pattern_dict():
   print("Coming soon... Returning to menu :)")
   print()
   menu()

def end():
   print("Thank you for using the Rubik's Cube help desk.")
   input("Press ENTER to quit.")

def menu():
  option = int(input("""Welcome to the Rubik's Cube help desk! Here are your options:
  1. Notations dictionary
  2. Scrambler
  3. Patterns dictionary
  4. Quit
  
  How can we help you today [1-4]? """))
  print()
  if option == 1:
     print(not_dict())
  elif option == 2:
     print(gen_scramble())
     print()
     repeat = input("Would you like another scramble (y/n)? ")
     while repeat == "y" or repeat == "yes":
        print(gen_scramble())
        print()
        repeat = input("Would you like another scramble (y/n)? ")
     print()
     print("Very well. Returning to menu...")
     print()
     menu()
  elif option == 3:
     print(pattern_dict())
  elif option == 4:
     print(end())
menu()