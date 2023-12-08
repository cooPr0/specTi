def ciagFibonaciego(n: int):
    a, b = 1, 1
    for i in range(n - 1):
        print(a, end=' ')
        b += a
        a = b - a
    return a

n = int(input("Podaj nr liczby z ciągu Fibonacciego: "))

print(ciagFibonaciego(n))




