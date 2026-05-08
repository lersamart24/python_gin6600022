fruit = {"apple": 25,
        "sugar apple": 30,
        "malon": 43,}
while True:
    pick = input("what fruit you want to buy from the list (apple/sugar apple/malon")
    
    if pick == "apple":
        print("Oh its",fruit["apple"],"baht")
        break
    
    elif pick == "sugar apple":
        print("it",fruit["sugar apple"],"baht")
        break
    elif pick == "malon":
        print("it",fruit["malon"],"baht")
        break
    else:
        print("oh i dont have that pick something we have")
