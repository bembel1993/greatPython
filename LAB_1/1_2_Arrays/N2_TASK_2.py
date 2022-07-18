P = int(input("Realized products in first day\n"))
Q = int(input("Limit "))
print("P = {0}".format(P))
print("Q = {0}".format(Q))
counter = (P/100)*3
print("Percent from {0} is {1}".format(P, counter))

while P <= Q:
    P += counter
    print(P)

