def details():
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
  return (csize, slen)

def menu():
    option = int(input("""Welcome to the Rubik's Cube help desk! Here are your options:
  1. Notations dictionary
  2. Scrambler
  3. Patterns dictionary
  4. Quit

  How can we help you today [1-4]? """))
    print()
    if option == 1:  # notation dictionary
        print(not_dict())
    elif option == 2:  # scrambler
        csize, slen = details()
        print(gen_scramble(csize, slen))
        print()
        repeat = input("Would you like another scramble (y/n)? ")
        while repeat == "y" or repeat == "yes":
            same = input("Same details (y/n)? ")
            print()
            if same == "y" or same == "yes":
                print(gen_scramble(csize, slen))
            else:
                csize, slen = details()
                print(gen_scramble(csize, slen))
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

def end():
   print("Thank you for using the Rubik's Cube help desk.")
   input("Press ENTER to quit.")