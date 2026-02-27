import random
animal = ("lion","tiger","elephant","monkey","panda")
print(animal)
pick = input("what your name")
random = random.choice(animal)
guess = input("the animal from the list")
if guess.lower() == random.lower():
    print("you win")
    print("The computer picks this: ",random)
else:
    print("you lose")
    print("The computer picks this: ",random)
