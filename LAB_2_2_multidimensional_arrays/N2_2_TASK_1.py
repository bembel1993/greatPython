# 1.	В матрице найти номер строки, сумма чисел в которой максимальна.
import random

from pip._vendor.msgpack.fallback import xrange

a = [[], []]

n = int(input("LIST INTEGER NUMBER 'i' :\n"))
m = int(input("LIST INTEGER NUMBER 'j' :\n"))

for i in xrange(0, n):
    c = random.randint(0, n)
    a.append([c])
    for j in xrange(0, m):
        d = random.randint(0, m)
        a[-1].append(d)
        print(a)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

for i in range(len(a)):
    x = 0
    s = 0
    sum = 0
    for j in range(len(a[i])):
        sum += a[i][j]
        if s<=sum:
            x = i
            s = sum

print(x)
print("Sum:", sum)
