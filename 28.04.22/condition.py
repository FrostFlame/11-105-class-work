from queue import Queue
from threading import Condition, Thread
from time import sleep

cond = Condition()
q = Queue()


def order_processor(name):
    while True:
        with cond:
            cond.wait_for(lambda: q)

            try:
                order = q.get()
                print(f'{name}: {order}')

                if order == 'stop':
                    break
            except:
                pass

            sleep(0.1)


Thread(target=order_processor, args=('thread 1',)).start()
Thread(target=order_processor, args=('thread 2',)).start()
Thread(target=order_processor, args=('thread 3',)).start()
sleep(10)

for i in range(10):
    q.put(f'order {i}')

for _ in range(3):
    q.put('stop')
