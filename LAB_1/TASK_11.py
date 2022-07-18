print("Enter number of threes: ")
a = int(input())
b = int(input())
c = int(input())
print("NUMBER OF THREES = {0}{1}{2}".format(a,b,c))
if (a>b and a>c):
    print("Many number is a")
    print("d = a = {0}".format(a))
elif (b>a and b>c):
    print("Many number is a")
    print("d = b = {0}".format(b))
elif (c>a and c>b):
    print("Many number is a")
    print("d = c = {0}".format(c))