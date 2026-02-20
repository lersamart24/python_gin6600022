x = int(input("Enter a number: "))
if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")

# Food Selection
x = input("what do you want to eat? (pizza/burger): ")
if x == "pizza":
 print("you chose pizza")
elif x == "burger":
 print("you chose burger")
else:
 print("Invalid choice")


# Street Food Story
import time
print("A boy named Sup was walking to school")
time.sleep(2)
print("His mom gave him 18 baht")
time.sleep(2)
shop = input("Did Sup find street food? (yes/no): ")
if shop == "yes":
 print("You found street food!")
 steet = input("Where to go — taco or burger? ")
 if steet == "taco":
 taco = int(input("How much for one taco (5/10/20): "))
 if taco == 5:
 print("I buy three")
 elif taco == 10:
 print("I buy two")
 else:
 print("I don't have that much money")
 else:
 burger = int(input("How much for one burger (10/20): "))
 if burger == 10:
 print("I buy one")
 else:
 print("I don't have that much money")
else:
 print("You walk to school with no food")


# Random Number Game
import time
from random import randint

print("Chat Sup GPT")
num = int(input("Pick a number 1–3: "))
time.sleep(1)
sup_gpt = randint(1, 3)
print("Chat Sup GPT picks", sup_gpt)


if num == sup_gpt:
    print("You win!")
else:
    print("You lose!")
