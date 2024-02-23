file = open("pi.txt").read()

lines = file.split("\n")

m = ""
d = ""
i = 0
lista = []
for el in range(0, len(lines) - 2):
    m = "".join(lines[el])
    v = "".join(lines[(el + 1)])
    d = "" + m + "" + v + ""
    lista.append(d)

    if int(d) > 90:
        i += 1

lista.sort()
najw = 0
najwLicz = 0
najmLicz = 0
najm = 0
print(lista)


for i in range(0, 100):
    licz = ""
    if i < 10:
        licz = lista.count("0" + str(i))
    else:

        licz = lista.count(str(i))
    if najw < licz:

        najwLicz = i
        najw = licz
    else:
        if najmLicz == 0:
            najmLicz = i
            najm = licz
        else:
            if najm > licz:
                najmLicz = i
                najm = licz
print("Najwieksza liczba: " + str(najwLicz) + " z liczba powtorzen: " + str(najw))
print("Najmniejsza liczba: " + str(najmLicz) + " z liczba powtorzen: " + str(najm))




