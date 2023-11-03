def czy_doskonala(n: int):

    lista = []

    for x in range(2, n):
        if n % x == 0:
            lista.append(n / x)

    suma = 1

    for y in lista:
        suma += y

    if suma == n:
        print("Liczba", n, "jest doskonala")
    else:
        print("Liczba", n, "nie jest doskonala")

czy_doskonala(289)
