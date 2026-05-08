contacts = {"mom": 1964,
           "dad": 3453,
           "sister": 4235,}
while True:
    call_list = input("Who do you want to call in the following list (mom/dad/sister")

    if call_list == "mom":
        print("you call your mom but she say why did you call so late it 11:00 pm. so here your mom number", contacts["mom"])
        break
    elif call_list == "dad":
        print("You call your dad but he was sleeping but here your dad number",contacts["mom"])
        break
        
    elif call_list == "sister":
        print("your calling your sister and she say stop calling your stop calling",contacts["sister"])
        break
    else:
        print("you didn't call from the contracts list TRY CALLING FROM THE CONTRACTS LIST")
