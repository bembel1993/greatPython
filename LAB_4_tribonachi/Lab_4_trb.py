cout = 1
num1 = 1
num2 = 1
num3 = 1

limit = int(input("Enter limit for digits of Tribonachi: "))

print(num1)
print(num2)

for count in range(limit):
    result = num1 + num2 + num3
    print(num3)
    num1 = num2
    num2 = num3
    num3 = result