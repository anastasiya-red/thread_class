from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        print(f'Sir {self.name}, на нас напали!')
        sleep(1)
        enemies = 100
        days = 0
        while enemies != 0:
            enemies -= self.skill
            days += 1
            print(f"Sir {self.name}, сражается {days} день(дня), осталось {enemies} воинов", flush=True)
            sleep(1)
        if enemies == 0:
            print(f'Sir {self.name} одержал победу спустя {days} дней!', flush=True)


knight1 = Knight("Lancelot", 10)
knight2 = Knight("Galahad", 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()


print('Все битвы закончились!')
