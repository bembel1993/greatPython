# 1. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными
# пользователем сторонами a и b на квадраты с наибольшей возможной на каждом
# этапе стороной. Выведите длины ребер получаемых квадратов и кол-во
# полученных квадратов.

def squares(a, b, n=0):
    if (a == b):
        return n + 1
    if (a < b):
        c = b - a
        d = n + 1
        print('Result a < b')
        print(a, c, d)
        print(n)
        return squares(a, b - a, n + 1)
    if (a > b):
        c = a - b
        d = n + 1
        print('Result a > b')
        print(c, b, d)
        print(n)
        return squares(a - b, b, n + 1)


a = int(input("Enter number --a--:"))
b = int(input("Enter number --b--:"))

print('Side --a-- : ' )
print(a)
print('Side --b-- : ' )
print(b)

print(squares(a, b))
