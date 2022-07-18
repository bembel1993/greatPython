print("Enter number of threes:\n ")
a = int(input())
b = int(input())
c = int(input())
if (a == 0 or a == 9) or (b==0 or b==9) or (c==0 or c==9):
    print("Really, this number {0}{1}{2} have null or nine".format(a,b,c))
else:
    print("This number {0}{1}{2} have not null or nine".format(a,b,c))