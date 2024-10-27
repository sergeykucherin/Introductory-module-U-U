first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second == third:
    print(3)
elif first == second and first != third or first != second and first == third or second == third:
    print(2)
elif first != second and first != third and second !=third:
    print(0)
