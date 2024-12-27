
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(line) for line in first_strings if len(line) >= 5]
second_result = [(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
combined_lists = first_strings + second_strings
third_result = {x: len(x) for x in combined_lists if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
