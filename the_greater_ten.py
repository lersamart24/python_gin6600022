number = []
num1 = int(input("pick a number"))
number.append(num1)
num2 = int(input("pick a number again"))
number.append(num2)
num3 = int(input("pick a number again"))
number.append(num3)
num4 = int(input("pick a number again"))
number.append(num4)
num5 = int(input("pick a number again last time"))
number.append(num5)
print(number)

for g in number:
    if g > 10:
        print(g)
