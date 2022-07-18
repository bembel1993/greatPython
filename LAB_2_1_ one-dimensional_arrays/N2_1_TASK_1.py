#Введите одномерный целочисленный список.
#Найдите наибольший нечетный элемент.
#Найдите минимальный по модулю элемент списка.
import random


n = int(input("LIST INTEGER NUMBER 'A' :\n"))
mas = []
A = []
B = []
equal = []
uneven = 0
for i in range(n):
    c = random.randint(0, n)
    mas.append(c)
    A = mas[i]
    print(A)
print("----------------------------------")
for i in mas:
    print(i)

for i in mas:
    if i % 2 != 0 & i > -1:
        print("UNEVEN ELEMENT OF ARRAYS ")
        uneven = i
        equal.append(uneven)
        print(equal)

maxNum = max(equal)
print("Max Number from a uneven array:", maxNum)
minNum = min(equal)
print("Min Number from a uneven array:", minNum)
