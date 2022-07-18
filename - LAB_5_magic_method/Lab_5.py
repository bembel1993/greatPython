class Tribonachi():
    cout = 1
    num1 = 0
    num2 = 0
    num3 = 0

    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def iterationMethod(self, limit):
        for count in range(limit):
            result = self.num1 + self.num2 + self.num3
            print(self.num3)
            self.num1 = self.num2
            self.num2 = self.num3
            self.num3 = result

limit = int(input("Enter limit for digits of Tribonachi: "))

tribonachi = Tribonachi(1, 1, 1)
print(1)
print(1)
tribonachi.iterationMethod(limit)
