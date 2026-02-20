import random
import time

rock = 1
scissors = 2
paper = 3

pick = input("pick one between /rock/paper/scissors")
ai = random.randint(1, 3)

if ai == 1:
 ai = "rock"
elif ai == 2:
 ai = "scissors"
else:
 ai = "paper"
  print("ai pick", ai)
if pick == ai:
    print("draw")
elif pick == "rock" and ai == "scissors":
    print("you win")
elif pick == "paper" and ai == "rock":
    print("you win")
elif pick == "scissors" and ai == "paper":
    print("you win")
else:
    print("you lose")
print("end game")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
