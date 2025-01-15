# Задача "Многопроцессное считывание"

import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_at = datetime.datetime.now()
for file in filenames:
    read_info(file)
end_at = datetime.datetime.now()
elapsed = end_at - start_at
print(elapsed, "(линейный)")

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        start_at = datetime.datetime.now()
        pool.map(read_info, filenames)
        end_at = datetime.datetime.now()
        elapsed = end_at - start_at
        print(elapsed, "(многопроцессный)")
