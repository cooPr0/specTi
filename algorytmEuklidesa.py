def algorytmEuklidesa(a: int, b: int):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    print(a)


algorytmEuklidesa(6, 9)
