immutable_var = 'fruit', 5, 3, 'vegetable', True
print(immutable_var)
#immutable_var[2] = 4
#print(immutable_var)
#   Значения элементов кортежа нельзя изменить, т.к. кортежи часто используются в качестве хранилищ данных, особенно
# когда необходимо сохранить список в неизменном виде,например, для сохранения географических координат. Долготу и
# широту города следует сохранить в кортеже, поскольку эти значения никогда не изменятся, а сохранение в кортеже будет
# гарантировать, что другие части программы случайно их не изменят.
mutable_list = [5, 'pear', True, 'London', 'Pyton']
mutable_list[0] = 'coconut'
mutable_list.append(39)
mutable_list.extend(['Double'])
mutable_list.remove('London')
print(mutable_list)

