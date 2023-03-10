import random

csize = int(input("Enter cube size [number only]: ")) #cube size
slen = random.randint(15, 25) #length of scramble 
moves = ["L", "R", "U", "D", "F", "B", "M", "x", "l", "r", "u", "d", "f", "b"]
mdir = ["", "'", "w"] #move direction
mcount = ["", "2"] #move count

if csize < 3:
  moves = moves[:6] + list(moves[7])
elif csize == 3:
  moves = moves[:8]
else:
  moves = moves

def gen_scramble():
  s = valid([[random.choice(moves), random.choice(mdir), random.choice(mcount)] for i in range(slen)])
  return ''.join(s[x][0] + s[x][1] + s[x][2] + " "for x in range(len(s)))

def valid(ar):
  for x in range (0, len(ar)):
    if ar[x][0] in moves[-7:-1]:
      ar[x][1] = random.choice(mdir[:2])
  for x in range(1, len(ar)):
      while ar[x][0] == ar[x-1][0]:
          ar[x][0] = random.choice(moves)
  for x in range (2, len(ar)):
      while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
          ar[x][0] = random.choice(moves)
  return ar

print((str(csize) + "x")*2 + str(csize) + " Scramble" + " - " + str(slen) + " steps" )
print(gen_scramble())