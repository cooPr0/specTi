def convert_number(number: int, system: int):

    print("Liczba w systemie dziesietnym:", number)
    result: list = []

    while number != 0:
        if number < system:
            if number >= 10:
                if number == 10:
                    result.append("A")
                if number == 11:
                    result.append("B")
                if number == 12:
                    result.append("C")
                if number == 13:
                    result.append("D")
                if number == 14:
                    result.append("E")
                if number == 15:
                    result.append("F")
            else:
                result.append(str(number))
            break

        mod = number % system

        result.append(str(mod))

        number = int(number / system)

    result = result[::-1]

    correct_result: str = ''

    for x in result:
        correct_result = correct_result + x

    print("Liczba w systemie (", system, "):", correct_result)


convert_number(10, 4)
