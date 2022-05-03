from threading import Lock, Thread
from time import sleep

lock1 = Lock()
lock2 = Lock()


def foo():
    while True:
        # with lock1:
        #     with lock2:
        #         print('foo')
        #         sleep(1)
        lock1.acquire(timeout=0.2)
        lock2.acquire(timeout=0.2)
        print('foo')
        sleep(2)
        lock2.release()
        lock1.release()



def bar():
    while True:
        # with lock2:
        #     with lock1:
        #         print('bar')
        #         sleep(1)
        lock2.acquire(timeout=0.2)
        lock1.acquire(timeout=0.2)
        print('bar')
        sleep(1)
        lock1.release()
        lock2.release()


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()
