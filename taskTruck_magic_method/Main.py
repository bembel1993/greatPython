class TableFact(str):
    def __init__(self, mass):
        self.mass = mass

    def __str__(self):
        #__str__ магический метод возвращающий строку
        return "mass Table: {} ".format(self.mass)

    def __add__(self, other):
        print("Sum of table: ", other + self.mass)
        return other + self.mass

class Truck():
    table_list =[]
    def __init__(self, lM):
        self.loadMax = lM

    def __str__(self):
        return "Max load truck: {} ".format(self.loadMax)

    def equqlLoadTruckAndMassTable(self, numberTable):
        if numberTable.mass <= self.loadMax:
            print("Truck pass for this table: ", str(numberTable.mass), " < ", self.loadMax)
        if numberTable.mass >= self.loadMax:
            print("Truck not pass for this table: ", str(numberTable.mass), " > ", self.loadMax)

truck = Truck(50)

tableFact_1 = TableFact(10)
tableFact_2 = TableFact(30)
tableFact_3 = TableFact(100)

twoAddTableFact = tableFact_1 + tableFact_3

print(twoAddTableFact)
print(truck)
print(tableFact_1)

truck.equqlLoadTruckAndMassTable(tableFact_2)
truck.equqlLoadTruckAndMassTable(tableFact_1)
truck.equqlLoadTruckAndMassTable(tableFact_3)

print("-----------------------------------------------")
truck.equqlLoadTruckAndMassTable(twoAddTableFact)
