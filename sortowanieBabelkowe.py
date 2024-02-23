lista = [3, 64, 47, 95, 2, 11, 90, 59, 35, 806, 256, 126, 1, 467, 655]


def sortowanieBabelkowe(list: list):
    for m in range(len(list)):
        for n in range(0, len(list) - 1):
            if (lista[n] > lista[n + 1]):
                lista[n], lista[n + 1] = lista[n + 1], lista[n]
    print(list)


sortowanieBabelkowe(lista)
