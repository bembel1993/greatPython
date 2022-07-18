m = int(input("Enter number m :\n "))
n = int(input("Enter number n :\n "))
p = int(input("Enter number p :\n "))
if (m<0 and (n>=0 and p>=0)) or (n<0 and (m>=0 and p>=0)) or (p<0 and (n>=0 and p>=0)):
    print("here are one number negative")
elif m<0 and n<0 and p<0:
    print("here are three number negative")
elif (m>=0 and (n<0 and p<0)) or (n>=0 and (m<0 and p<0)) or (p>=0 and (n<0 and p<0)):
    print("here are two number negative")
else:
    print("It's alright, not negative number")