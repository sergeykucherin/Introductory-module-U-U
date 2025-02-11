
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()               # без аргументов вызов функции работает, т.к. аргументы именованные и уже заданы
                             # в параметрах функции. Вывод в консоль: 1 строка True;

# print_params(2, 3, 4, 5)   # с разным количеством аргументов в вызове функции выходит ошибка, что аргументов задано
                             # больше, чем принимает данная функция;

print_params(b = 25)         # вызов функции работает, т.к. мы просто переименовали значение параметра <b>.
                             # Вывод в консоль: 1 25 True;

print_params(c = [1, 2, 3])  # вызов функции работает, т.к. мы просто переименовали значение параметра <c>.
                             # Вывод в консоль: 1 строка [1, 2, 3];

values_list = [58, 'apple', [1,7,9]]
values_dict = {'a': 891355347, 'b': 89583485664, 'c': 89605473261}

print_params(*values_list)   # вызов функции работает, вывод в консоль: 58 apple [1, 7, 9];

print_params(**values_dict)  # вызов функции работает, вывод в консоль: 891355347 89583485664 89605473261;

values_list_2 = [37, 'Fruit']

print_params(*values_list_2, 42)     # вызов функции работает, т.к. изначально в функции задано 3 параметра и данный
                                        # список распаковался в 2 параметра + 1 параметр был задан в вызове. Вывод в
                                        # консоль: 37 Fruit 42.











