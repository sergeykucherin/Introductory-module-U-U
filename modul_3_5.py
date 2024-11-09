#Задача "Рекурсивное умножение цифр"
from math import factorial


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    while str_number.endswith('0'):
        str_number = str_number[:len(str_number) - 1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))

    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(420)
print(result)
# result = get_multiplied_digits(101)
# print(result)
#
# result = get_multiplied_digits(25)
# print(result)