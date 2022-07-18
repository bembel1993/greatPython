a = int(input("Enter number a :\n "))
b = int(input("Enter number b :\n "))
c = int(input("Enter number c :\n "))
if a==b==c:
    print ("Here have three equals number")
elif (a and (b==c)) or (b and (a==c)) or (c and (a==b)):
    print ("Here have two equals number")
elif a != b or b !=c or c!=a:
    print("Not equals number")
