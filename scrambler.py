class Scrambler:
    def gen_scramble(self, csize, slen):
      print((str(csize) + "x")*2 + str(csize) + " Scramble" + " - " + str(slen) + " steps" )
      s = valid([[random.choice(moves[csize]), random.choice(mdir), random.choice(mcount)] for i in range(slen)], csize)
      return ''.join(s[x][0] + s[x][1] + s[x][2] + " "for x in range(len(s)))

    def valid(self, ar, csize):
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