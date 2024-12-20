import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        day = 0
        rivals = 100
        print (f'{self.name}, на нас напали!')
        while rivals > 0:
            rivals -= self.power
            day += 1
            time.sleep(1)
            print(f"{self.name} сражается {day} день(дня), осталось {rivals} воинов.")
        else:
            print(f"{self.name} одержал победу спустя {day} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')



