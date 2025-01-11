# Задача "За честь и отвагу!"

import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.days = 0
        self.enemy = 100

    def timer(self, name, days, enemy):
        while self.enemy > 0:
            time.sleep(1)
            self.days += 1
            self.enemy -= self.power
            print(f'{self.name} сражается {self.days} день(дня), осталось {self.enemy} воинов.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.timer(self.name, self.days, self.enemy)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")