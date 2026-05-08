pet_center = {
    "names": ["Bob", "Silver", "Gold"],
    "species": ["Stray Dog", "Stray Cat", "Bird"],
    "toys": ["Rubber toy", "Bird", "Mimicking toy"]
}

pet = input("what  pet do you want from the list (dog/bird/cat)").lower()
if pet == "dog":
    print("Its name is",pet_center["names"][0])
    print("Its a",pet_center["species"][0])
    print("He plays with",pet_center["toys"][0])

elif pet == "cat":
    print("Its name is",pet_center["names"][1])
    print("Its a",pet_center["species"][1])
    print("He plays with",pet_center["toys"][1])

elif pet == "bird":
    print("Its name is",pet_center["names"][2])
    print("Its a",pet_center["species"][2])
    print("He plays with",pet_center["toys"][2])

else:
    print("just get out of my shop")
