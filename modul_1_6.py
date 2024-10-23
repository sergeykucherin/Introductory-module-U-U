my_dict = {'Oleg': 1973, 'John': 1999, 'Igor': 2005, 'Sarah': 2007}
print(my_dict)
print(my_dict['John'])
print(my_dict.get('Sasha'))
my_dict.update({'Nataly': 1975, 'Nadia': 1984})
a = my_dict.pop('Oleg')
print(a)
print(my_dict)

my_set = {'Fruit', 1, 2, 1.7, 2, 'Fruit', 1, ('Fruit', 1, 1.7), False}
print(my_set)
my_set.update((8, 'String'))
my_set.discard(2)
print(my_set)