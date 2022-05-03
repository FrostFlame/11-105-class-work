import random
from threading import Condition, Thread
from time import sleep

my_queue = []
capacity = 10

condition = Condition()


class Producer(Thread):
    def run(self):
        global my_queue
        tokens = range(10, 50)

        while True:
            with condition:
                if len(my_queue) == capacity:
                    print('Очередь заполнена, производитель - жди')
                    condition.wait()
                    print('Появилось свободное место, потребитель уведомил производителя')
                token = random.choice(tokens)
                my_queue.append(token)
                print('Производитель добавил', token)
                condition.notify()
            sleep(1)


class Consumer(Thread):
    def run(self):
        global my_queue

        while True:
            with condition:
                if len(my_queue) == 0:
                    print('Очередь пустая, потребитель - жди')
                    condition.wait()
                    print('Потребитель добавил в очередь и уведомил потребителя')
                token = my_queue.pop(0)
                print('Потребитель получил', token)
                condition.notify()
            sleep(2)


t1 = Producer().start()
t2 = Consumer().start()
