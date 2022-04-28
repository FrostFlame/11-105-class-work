from threading import Thread
from time import sleep


def func(n):
    for i in range(n):
        print(f'from child thread: {i}')
        sleep(0.5)


th = Thread(target=func, args=(5,), daemon=True)
th.start()
sleep(1)
print("App stop")
