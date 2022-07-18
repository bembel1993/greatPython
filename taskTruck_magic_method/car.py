class Car:

    def __init__(self, mark, speed):
        self.mark = mark
        self.speed = speed

    def __str__(self):
        return "mark: {} \nspeed: {} km/ch".format(self.mark, self.speed)

bmv = Car("BMV", 200)
print(bmv)