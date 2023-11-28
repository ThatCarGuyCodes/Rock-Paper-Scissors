from getpass import getpass as input

print("Choose your move (R/P/S) ")
p1 = input("Player 1: ")
p2 = input("Player 2: ")

if p1 == "R":
  if p2 == "R":
    print("Tie! 👔")
  elif p2 == "S":
    print("P1's Rock 🪨 crushes P2's Scissors ✂️")
  elif p2 == "P":
    print("P2's paper 📝 ends P1's Rock 🪨")
  else:
    print("Use R, P, or S")
if p1 == "P":
  if p2 == "R":
    print("P1's paper 📝 ends P2's rock 🪨")
  elif p2 == "S":
    print("P2's scissors ✂️ cut P1's paper 📝")
  elif p2 == "P":
    print("Tie! 👔")
  else:
    print("Use R, P, or S")
if p1 == "S":
  if p2 == "R":
    print("P2's rock 🪨 crushes P1's scissors ✂️")
  elif p2 == "S":
    print("Tie! 👔")
  elif p2 == "P":
    print("P1's scissors ✂️ cuts P2's paper 📝")
  else:
    print("Use R, P, or S")
