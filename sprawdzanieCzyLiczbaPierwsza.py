import math

def czy_pierwsza(n: int):
    if n < 2:
        print("Liczba nie jest liczba pierwsza")

    dzielnik = int(math.sqrt(n))

    for x in range(2, dzielnik):
        if n % x == 0:
            print("Liczba", n, "nie jest liczba pierwsza")
            return False
        x += 1

    print("Liczba", n, "jest liczba pierwsza")

czy_pierwsza(7)
