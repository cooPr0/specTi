def convert_number(number: str, system: int):

    print("Liczba w systemie (", system, "):", number)

    w = 1

    result = 0

    number = number[::-1]

    for letter in number:
        if letter == ('A' or 'B' or 'C' or 'D' or 'E' or 'F'):
            if letter == 'A':
                result += w * 10
            if letter == 'B':
                result += w * 11
            if letter == 'C':
                result += w * 12
            if letter == 'D':
                result += w * 13
            if letter == 'E':
                result += w * 14
            if letter == 'F':
                result += w * 15
        else:
            result += w * int(letter)

        w = w*system

    print("Liczba w systemie dziesietnym:", result)


convert_number('101', 3)
