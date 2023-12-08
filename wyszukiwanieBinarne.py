zbior = [1, 2, 3, 3, 4, 5, 7, 8, 9, 11, 23, 23, 24, 33, 36, 67, 117, 356, 678]

def wyszukiwanieBinarne(ciag, szukana: int):
    index = 0
    porownanie = len(ciag) - 1
    while index <= porownanie:
        srodek = (index + porownanie) // 2
        if szukana == ciag[srodek]:
            return  print("Szukana liczba to: ", szukana)
        if szukana > ciag[srodek]:
            index = srodek + 1
        if szukana < ciag[srodek]:
            porownanie = srodek - 1

    return print("Nie znaleziono szukanej liczby")

szukana = int(input("Podaj szukana liczbe: "))

wyszukiwanieBinarne(zbior, szukana)

