import time
import random

water = 1
fire = 2
wood = 3
thunder = 4

hm = input("pick one between fire/water/wood/thunder: ").lower()
ai = random.randint(1, 4)

if ai == 1:
 ai = "water"
 print("water")
elif ai == 2:
 ai = "fire"
 print("fire")
elif ai == 3:
 ai = "wood"
 print("wood")
else:
    ai = "thunder"
    print("thunder")

if ai == hm:
    print("draw")
elif ai == "fire" and hm == "water":
    print("you win")
elif ai == "water" and hm == "thunder":
    print("you win")
elif ai == "wood" and hm == "fire":
    print("you win")
elif ai == "thunder" and hm == "wood":
    print("you win")
elif ai == "water" and hm == "wood":
    print("you win")
elif ai == "thunder" and hm == "fire":
    print("you win")
else:
    print("you lose")
