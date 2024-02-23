file = open("pi.txt").read()

lines = file.split("\n")

m = ""
d = ""
i = 0
for el in range(0, len(lines) - 2):
    m = "".join(lines[el])
    v = "".join(lines[(el + 1)])
    d = "" + m + "" + v + ""
    if int(d) > 90:
        i += 1
print(i)

