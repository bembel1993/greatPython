print("     ENTER QTY MUSHROOM: ");
K = int(input())

if ((K == 1 or K == 21 or K == 31 or K == 41 or K == 51 or K == 61 or K == 71 or K == 81 or K == 91 or K == 101)
        and(K < 120)):
    print("Мы нашли {0} гриб в лесу.".format(K))
if (K >= 2 and K <= 4) or (K >= 22 and K <= 24) or (K >= 32 and K <= 34) or (K >= 42 and K <= 44) \
    or (K >= 52 and K <= 54) or (K >= 62 and K <= 64) or (K >= 72 and K <= 74) or (K >= 82 and K <= 84) \
    or(K >= 92 and K <= 94) or (K >= 102 and K <= 104):
    print("Мы нашли {0} гриба в лесу.".format(K))
if(K >= 5 and K<=20) or (K>=95 and K <= 120):
    print("Мы нашли {0} грибов в лесу.".format(K))
