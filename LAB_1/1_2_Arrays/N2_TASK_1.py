import random
#1. Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
#Могут ли два билета подряд быть удачными?

a = int(input("Enter size of number:\n"))#6 two tickets - enter 12
mas = []
for i in range(a):
    n = random.randint(0, 9)
    mas.append(n)
for i in range(a):
    print(mas[i])
print("One ticket: ")
print(mas[0], mas[1], mas[2], mas[3], mas[4], mas[5])
print("Two ticket: ")
print(mas[6], mas[7], mas[8], mas[9], mas[10], mas[11])
sum=sum(mas)
print(sum)

if sum%7 == 0:
    for i in range(a):
        print(mas[i])
    print("Yes, tickets cann be lucky")
else:
    print("No, two tickets can not be lucky!")