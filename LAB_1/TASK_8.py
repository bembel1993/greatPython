print("Enter number of FOUR")
print(" and you will know digits this number equals between themselves:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("You enter next number {0}{1}{2}{3}".format(a,b,c,d))
if (a!=b and a!=c and a!=d) and (b!=a and b!=c and b!=d) and (c!=a and c!=b and c!=d) and (d!=a and d!=b and d!=c):
    print("Yes, this digits not equals between themselves")
else:
    print("This number have digits wich equals between themselves")
