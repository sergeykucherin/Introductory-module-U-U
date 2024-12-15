import io
file_name = 'test_file.txt'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write("It's a text for task Найти везде,\nИспользуйте его для самопроверки.\nУспехов в решении задачи!"
               "\ntext text text")

file_name = 'Rudyard Kipling - If.txt'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write('If\n'
                '\n'
                'If you can keep your head when all about you\n'
                '   '   'Are losing theirs and blaming it on you,\n'
                'If you can trust yourself when all men doubt you,\n'
                '   '    'But make allowance for their doubting too;\n'
                'If you can wait and not be tired by waiting,\n'
                '   '    'Or being lied about, don’t deal in lies,\n'
                'Or being hated, don’t give way to hating,\n'
                '   '    'And yet don’t look too good, nor talk too wise:\n'
                '\n'
                'If you can dream — and not make dreams your master;\n'
                '   '    'If you can think — and not make thoughts your aim;\n'
                'If you can meet with Triumph and Disaster\n'
                '   '    'And treat those two impostors just the same;\n'
                'If you can bear to hear the truth you’ve spoken\n'
                '   '    'Twisted by knaves to make a trap for fools,\n'
                'Or watch the things you gave your life to, broken,\n'
                '   '    'And stoop and build ’em up with worn-out tools:\n'
                '\n'
                'If you can make one heap of all your winnings\n'
                '   '    'And risk it on one turn of pitch-and-toss,\n'
                'And lose, and start again at your beginnings\n'
                '   '    'And never breathe a word about your loss;\n'
                'If you can force your heart and nerve and sinew\n'
                '   '    'To serve your turn long after they are gone,\n'
                'And so hold on when there is nothing in you\n'
                '   '    'Except the Will which says to them: ‘Hold on!’\n'
                '\n'
                'If you can talk with crowds and keep your virtue,\n'
                '   '    'Or walk with Kings — nor lose the common touch,\n'
                'If neither foes nor loving friends can hurt you,\n'
                '   '    'If all men count with you, but none too much;\n'
                'If you can fill the unforgiving minute\n'
                '   '    'With sixty seconds’ worth of distance run,\n'
                'Yours is the Earth and everything that’s in it,\n'
                '   '    'And — which is more — you’ll be a Man, my son!\n'
                '\n'
                'Rudyard Kipling')

class WordsFinder:
    file_names = ()
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                punctuation = str([',', '.', '=', '!', '?', ';', ':', ' - '])
                all_words[name] = file.read().lower().replace(punctuation, '').split()
        return all_words

    def find(self, word):
        new_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                new_dict[name] = words.index(word.lower()) + 1
        return new_dict

    def count(self, word):
        _dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
               _dict[name] = words.count(word.lower())
        return _dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Rudyard Kipling - If.txt')
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))