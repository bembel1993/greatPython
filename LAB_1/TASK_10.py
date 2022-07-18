print("Enter number of threes: ")
a = int(input())
b = int(input())
c = int(input())
SUM=(a+b+c)
if SUM%3 == 0:
    print("NUMBER OF THREES = {0}{1}{2}".format(a,b,c))
    print("Sum equals {0}".format(SUM))
    print("REALLY, sum this number {0}{1}{2} share at three".format(a,b,c))
else:
    print("NUMBER OF THREES = {0}{1}{2}".format(a, b, c))
    print("Sum equals {0}".format(SUM))
    print("This number {0}{1}{2} NOT share at three".format(a,b,c))