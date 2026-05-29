# try:
#     pick = int(input("what number do you like 1-10"))
#     pickk = int(input("what number do you like  1-10"))

#     num = pick // pickk 
    
#     print(num)

# except ValueError:
#     print("please enter something that is a number")

# except ZeroDivisionError:
#     print("You cannot divide by zero")



# age = None

# try:
#     age = int(input("What is your age? "))
    
#     if age < 0:
#         raise ValueError("kid.")
#     elif age == 0:
#         raise ValueError("Age cannot be zero.")
#     elif age >150:
#         raise ValueError("old")
#     elif age == 21:
#         raise ValueError("9 + 10")
    
# except ValueError as e:
    
#     print(e)

# finally:
#     print("I am free now!")


# try:
#     number = int(input("pick a number"))

# except ValueError:
#     print("Please enter a vaild number")

# finally:
#     print("nothing")



# try:
#     pick = int(input("Pick a random number you like"))
#     pickk = int(input("Pick again"))
    
#     num = pick // pickk
#     print(num)

# except ValueError:
#     print("Number not letter")

# except ZeroDivisionError:
#     print("don't pick 0 i guess")    
    
# egg = None
# try:
#     egg = int(input("what your age"))    
#     if egg <=0:
#         raise ValueError("Your age is 0 or  less then 0")
        
# except ValueError as e:
#     print(e)
   
    
# finally:
#     print("Age accepted")


# list = ["grape", "apple", "banana"]
# print(list)
# try:
#     fruit = int(input("what number you like 0/1/2"))
#     print(list[fruit])

# except IndexError:
#     print("wrong number")

# except ValueError:
#     print("pick the number in the list")
