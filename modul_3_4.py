
# Задача "Однокоренные"
# 1-й Вариант с использованием цикла While:

def single_root_words(root_word, *other_words):
    same_words = []
    count = 0
    while count < len(other_words):
        word = other_words[count]
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
        count += 1

    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))

# 2-й Вариант с использованием цикла For:

def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        i = other_words[i]
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)

    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))






# text = "banana"
# count_of_na = text.count("na")
# print(count_of_na)  # Вывод: 2

#Нужный метод для решения этой задачи:
# count = phrase. count(word) print(count > 0)

# authors = ("Толстой", "Чехов", "Пушкин")
# texts = ["псевдоним Чехова был А-т Чехонте", "Пушкин погиб в дуэли", "и тд"]
#
# found_count = sum(any(a in text for a in authors) for text in texts)
# print('Найдено совпадений:', found_count)

