def rozkladNaLiczbyNaturalne(liczba: int):

    dzielnik: int = 2

    if liczba < 2:
        print("Podana liczba to: ", liczba)

    while liczba >= 2:
        while liczba % dzielnik == 0:
            print(dzielnik)
            liczba = liczba / dzielnik
        dzielnik += 1


rozkladNaLiczbyNaturalne(456)
