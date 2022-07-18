from math import sqrt

a = int(input("Enter number a :\n "))
b = int(input("Enter number b :\n "))
c = int(input("Enter number c :\n "))
print("You find\n")
x = a + b + c
if x % 2 != 0:
    x = a * b * c
    s = sqrt(x)
    print("geometric mean\n")
    print(s)
    print("\nbecause not null")
elif x % 2 == 0:
    av = x / 2
    print("average\n")
    print(av)
    print("\nbecause equal null")
