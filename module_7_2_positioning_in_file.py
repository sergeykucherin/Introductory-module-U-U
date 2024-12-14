def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    str_num = 0
    for string in strings:
        byte_num = file.tell()
        file.write(string + '\n')
        str_num += 1
        key = (str_num, byte_num)
        strings_positions[key] = string
    file.close()
    return  strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)






