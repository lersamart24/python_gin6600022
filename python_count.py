import time
num_list = [2,4,4,6,2,4,9,7,6,3]
print(num_list)
number = input("do you want to check any of the number(yes/no)")
if number == "yes":
    list_number = int(input("what number do you want to check"))
    count_num = num_list.count(list_number)
    print(count_num)
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(0.7)
    print(".")
    time.sleep(0.7)
    print("that all")




else:
    print("that all")
