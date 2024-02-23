

def przedzial():
    f = open('przedzialy.txt')

    dane = f.read()
    dane = dane.split('\n')
    for x in dane:
        y = x.split(',')
        for z in y[0]:
            if z[1] == "-":
                break
            print(z)
        for z in y[1]:
            print(z)


    f.close()


przedzial()
