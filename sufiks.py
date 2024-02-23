plik = open("slowa3.txt", "r")
wiersze = plik.readlines()
lista= []
for wiersz in wiersze:
    lista.append(wiersz.strip().split(" "))


def czy_mniejszy(n, s, k1, k2):
    i = int(k1)
    j = int(k2)
    while i < n and j < n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return print("TAK")
            else:
                return print("NIE")
    if j <= n:
        print("TAK")
    else:
        print("NIE")

czy_mniejszy(int(lista[0][0]), lista[1][0], int(lista[2][0]), int(lista[2][1]))
