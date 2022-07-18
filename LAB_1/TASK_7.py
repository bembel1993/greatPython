Y = int(input("Enter NUMBER OF YEAR please :\n "))
print(" and you will find out what year it is ")
if Y%4 != 0:
    print("normal year")
elif Y%100 == 0:
    print("is century")
    if Y%400 == 0:
        print("this year intercalary year")
    else:
        print("normal year")
else:
    print("this year is intercalary year ")