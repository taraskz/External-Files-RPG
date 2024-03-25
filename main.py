from tabulate import tabulate

rooms = {
  "Main Hall": "In front of you is a long hall with expensive paintings and\
a long red carpet.",
  "Kitchen": "Now you're in the kitchen of the castle, it smells great",
  "Kings Room": "You are in the kings room where he sleeps, hes not here",
  "Dinning Room":"Now you're in the dinning room where the king eats",
  "Throne Room":"You ended up in the throne room where the king sits"
      }

room_location = {
  "Main Hall": (0,0), # start
  "Kitchen": (0,-1), # one down
  "Kings Room": (1,-1), # one down 1 right
  "Dinning Room": (0,-2), # two down
  "Throne Room": (1,0), # one right
  "Bathroom": (2,0) # two right

# external file name 
mapfile = "map.txt"


def read_map():
    