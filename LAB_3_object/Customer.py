class Customer:
    id = 0

    def __init__(self, id, las, fir, num, bal):
        self.id = id
        self.lastname = las
        self.firstname = fir
        self.number_credit_card = num
        self.balance = bal

    def get_id(self):
        return self.id
    def get_lastname(self):
        return self.lastname
    def get_firstname(self):
        return self.firstname
    def get_number_credit_card(self):
        return self.number_credit_card
    def get_balance(self):
        return self.balance

    def show(self, id, lastname, firstname,
               number_credit_card, balance):
        print("| ",id, "|", lastname, "  ", firstname,
               "       ", number_credit_card, "       ", balance)

    @staticmethod
    def headerTable():
        print("+------+------------+-------------+-------------+-----------+")
        print("|  ID  |  LastName  |  FirstName  |  Number CC  |  Balance  |")
        print("+------+------------+-------------+-------------+-----------+")

    @staticmethod
    def headerTable2():
        print("+-----+--------+---------+---------+-------+")
        print("|  ID |LastName|FirstName|Number CC|Balance|")
        print("+-----+--------+---------+---------+-------+")
