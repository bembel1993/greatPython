# Создать класс Customer: id, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, баланс.
# Функции - члены реализуют запись и считывание полей
# (проверка корректности), зачисление и списание сумм на счет.
# Создать список объектов. Вывести:
# a) список покупателей в алфавитном порядке;
# b) список покупателей, у которых номер кредитной карточки находится в заданном интервале.
import operator

from LAB_3_object.Customer import Customer

obj1 = Customer(102, "Давыдов", "Денис", 100002, 30000)
obj2 = Customer(103, "Кюхельбекер", "Вильгельм", 100034, 46000)
obj3 = Customer(104, "Языков", "Николай", 120300, 789000)
obj4 = Customer(105, "Батюшков", "Константин", 102070, 100000)
obj5 = Customer(106, "Рылеев", "Кондратий", 400990, 289000)
obj6 = Customer(107, "Баратынский", "Евгений", 451000, 342000)
obj7 = Customer(108, "Веневитинов", "Дмитрий", 101022, 92000)
ObjectArray = [obj1, obj2, obj3, obj4, obj5, obj6, obj7]  # Список экземпляров класса Customer
while True:

    resultList = ObjectArray
    result = sorted(ObjectArray, key=operator.attrgetter('lastname'))  # Сортировка по атрибуту lastname
    print(" ")
    print(" 1. Посмотреть списки Customers\n",
          "2. Списки покупателей в алфавитном порядке из массива\n",
          "3. Cписок покупателей, у которых номер кредитной карточки находится в заданном интервале\n",
          "4. Добавить Customers\n",
          "5. Проверка корректности, зачисление и списание сумм на счет\n",
          "6. Удаление покупателя\n",
          "7. Exite\n")
    choice = int(input("Enter menu number: "))

    if choice == 1:
        print("1. Просмотр списков покупателей")
        print("Вывод данных при помощи метода show() класса Customer")
        Customer.headerTable()
        obj1.show(obj1.id, obj1.lastname, obj1.firstname, obj1.number_credit_card, obj1.balance)
        print("Вывод данных из массива")
        Customer.headerTable2()
        for customer in resultList:
            print("|", customer.id, "|", customer.lastname, customer.firstname, customer.number_credit_card,
                  customer.balance)

    if choice == 2:
        print("2. Списки покупателей в алфавитном порядке из массива: ")
        Customer.headerTable2()
        for customer in result:
            print(customer.id, customer.lastname, customer.firstname, customer.number_credit_card, customer.balance)

    if choice == 3:
        print("3. Cписки покупателей, у которых номер кредитной карточки находится в заданном интервале: ")
        for customer in resultList:
            if  customer.number_credit_card >= 100000 | customer.number_credit_card <= 500000:
                customer.number_credit_card
                print(customer.number_credit_card)
            else:
                print("not this range")

    if choice == 4:
        print("4. Добавить Customers")
        id = int(input("Enter ID: "))
        fn = str(input("Enter first name: "))
        ln = str(input("Enter last name: "))
        ncc = str(input("Enter number credit card: "))
        balance = int(input("Enter balance: "))
        objNew = Customer(id, fn, ln, ncc, balance)

        newObjectArray = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, objNew]
        ObjectArray = newObjectArray
        print("New Customers is add: ")
        for customer in newObjectArray:
            print(customer.id, customer.lastname, customer.firstname, customer.number_credit_card, customer.balance)

    if choice == 5:
        print("5. Проверка корректности, зачисление и списание сумм на счет")
        ln = str(input("Enter last name: "))
        for customer in ObjectArray:
            if ln == customer.lastname:
                print("name correct ", ln)
                print(" 1. Зачислить деньги на счет\n",
                      "2. Списать деньги со счета")
                whatYouWantMake = int(input(" Enter position: "))
                if whatYouWantMake == 1:
                    print("5.1 Зачислить деньги на счет")
                    enterSum = int(input(" Enter sum: "))
                    resultSum = customer.balance + enterSum
                    customer.balance = resultSum
                    print("Вы зачислили деньги - ", resultSum)
                    print(customer.lastname, customer.balance)
                if whatYouWantMake == 2:
                    print("5.2 Списать деньги со счета")
                    enterSum = int(input(" Enter sum: "))
                    resultSum = customer.balance - enterSum
                    customer.balance = resultSum
                    print("Вы списали деньги - ", resultSum)
                    print(customer.lastname, customer.balance)
            else:
                print("not correct")

    if choice == 6:
        print("6. Удаление покупателя ")
        id = int(input("Enter id: "))
        print("Enter 0 for exit ")
        for customer in ObjectArray:
            if id == customer.id:
                print("id correct ", id, customer.lastname)
                customer.id = 0
                customer.lastname = "-"
                customer.firstname = "-"
                customer.number_credit_card = "-"
                customer.balance = "-"
            if id == 0:
                break
            else:
                print("not correct id")

    if choice == 7:
        break
