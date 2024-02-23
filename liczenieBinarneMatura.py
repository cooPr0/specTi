def liczenie():
    file = open("bin.txt").read()
    lines = file.split("\n")
    k = 0
    pop = ""

    for line in lines:
        if len(line) == len(pop):
            c = 0
            d = 0
            for j in line:
                if j == '0':
                    break
                c += 1
            for i in pop:
                if i == '0':
                    break
                d += 1
            if c > d:
                pop = line
        if len(line) > len(pop):
            pop = line


        b = 1

        for i in range(0, len(line) - 1):
            if line[i] != line[i + 1]:
                b += 1
        if (b <= 2):
            k += 1

    print(pop)
    print(k)


liczenie()

# def xor():
#     file = open("bin.txt").read()
#     lines = file.split("\n")
#
#     for p in lines:
#         p = int(p, 2)
#         print(p)
#         b = p ^ (p // 2)
#         print(b)
#     #     p = p[::-1]
#     #     w = 0
#         liczba = 0
#     #     for i in p:
#     #         liczba += int(i) * 2**w
#     #         w += 1
#     #     #liczba = liczba // 2
#         k = p // 2
#         m = []
#         while k > 1:
#             m.append(str(k % 2))
#             k = k // 2
#         m.append(str(k))
#         m = "".join(m)[::-1]
#         print("ggg", m)
#     #     p = p[::-1]
#     #     g = liczba ^ (liczba // 2)
#     #     print(g)
#
# xor()


