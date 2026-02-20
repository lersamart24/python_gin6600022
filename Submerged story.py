import time
# def no_respwan():
#     (game over)

def intro():

    name = input("What is your name: ")
    time.sleep(1)
    print(" ")
    print("Your name is",name)
    time.sleep(1)
    print()
    print("You have woke up from your dream")
    print(" ")
    time.sleep(1)
    print("Somthing is calling you")
    print(" ")
    time.sleep(1)
    print("You follow the sound")
    print(" ")
    time.sleep(1)
    part_one()
   
def part_one():
    while True:
        sea = input("It lead you to the beach (explore/stay): ").lower()
        if sea == "explore":
            print("You follow the the sound")
            print(" ")
            time.sleep(1)
            print("You got suck by a whirlpool")
            print(" ")
            time.sleep(1)
            print("You wake on the on the sea floor ")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            part_two()
            break

   
        elif sea == "stay":
            print("You stay home and keep sleeping")
            print("Game over")
            print("Better luck next time")
            break
           
        else:
            print("Worng choice try again")
            print(" ")
            time.sleep(1)
         
def part_two():
    print("You keep walking")
    print(" ")
    time.sleep(1)
    print("You accidentally step on a mysterious egg")
    print(" ")
    time.sleep(1)
    while True:
        oct = input("The ground shake tentacles start a appear out of no where (run/stand)").lower()
        time.sleep(1)
        print(" ")
        if oct == "run":
            print("A rock hit you while running and you die")
            print(" ")
            time.sleep(1)
            print("Better luck next time try again")
        elif oct == "stand":
            print("You got drag down by the tentacles")
            time.sleep(1)
            print(" ")
            print("The tentacles drag to Challenger Deep and you saw a fraction of the thing draging you down")
            challenger_deep()
            break
        else:
            print("You miss spell try again")
            print(" ")
            time.sleep(1)

def challenger_deep():
    while True:
        time.sleep(1)
        print(" ")
        guess = input("Guess what is dragging you down it big and have tentacles(kraken/cthulhu)").lower()
        if  guess == "kraken":
            print("You are correct ✓ kraken")
            kraken_one()
            break

        elif guess == "cthulhu":
            print("your worng ✕ ")
            print(" ")
            time.sleep(1)
        else:
            print("Worng you miss spell try  typing again!!")
            print(" ")
            time.sleep(1)

def kraken_one():
    print("The tentacles stop dragging you down")
    time.sleep(1)
    print(" ")
    while True:
        light = input("The tentacles vanish you can't see anything you found a light (go/stay)").lower()
        time.sleep(1)
        print(" ")
        if light == "go":
            print("You found a giant angler fish ")
            time.sleep(1)
            print(" ")
            print("it eat you adn you die")
            print("better luck next time try again :)")
        elif light == "stay":
            print("The light fade away")
            print("You found a speargun")
            lion_fish()
            break
        else:
            print("Look like you miss spell try again")
            Print(" ")
            time.sleep
           

def lion_fish():
    print("The lion fish charge at you")
    print(" ")
    time.sleep(1)
    while True:
        shoot = input("you got two choice right now one shoot the fish two hide under a rock (one/two)").lower()
        print(" ")
        time.sleep(1)
        if shoot == "two":
            print("you go hide under a rock but under a rock there a shark it eat you and die")
            print(" ")
            time.sleep(1)
            print("better luck next time")
        elif shoot == "one":
                print("You shot the lion fish you survived")
                print(" ")
                time.sleep(1)
                print("you hear something inside your head")
                megalodon()
                break
        else:
            print("You lke you miss spell try again")
            print(" ")
            time.sleep

def megalodon():
    print("The sound tell you that somthing big is coming your way")
    print(" ")
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print("After the swarm of fish pass you")
    print(" ")
    time.sleep(1)
    print("A giant fish is coming your say  ")  
    while True:
        move = input("A swarm of fish is coming your way(run/hide/fight)").lower()
        print(" ")
        time.sleep(1)
        if move == "run":
            print("You try to run but you trip over a stone")
            print(" ")
            time.sleep(1)
            print("Better luck next time")
        elif move == "hide":
            print("You try to hide under the sand but you got shock by the stingray")
            print(" ")
            time.sleep(1)
            print("better luck next time how many did i say this")
        elif move == "fight":
            print("Some how you fight the giant fish and win ")
            the_end()
            break
        else:
            print("look like you miss spell try again")
           


   
def the_end():
    print("You hear the sound of a clock")
    print(" ")
    time.sleep(1)
    print("You wake up from your deam and say(is it just a dream)")
    print(" ")
    time.sleep(1)
    print("Your mom call (Be fast you got school)")
    print(" ")
    time.sleep(1)
    print("The end")





intro()
