from threading import Thread, Lock, RLock

some_var = 0
lo = Lock()
# lo = RLock()


def some_func(id):
    with lo:
        global some_var
        print(f'{id} here!')
        for i in range(1000000):
            some_var += 1
        print(f'{id} leaving!')


t1 = Thread(target=some_func, args=(1,))
t2 = Thread(target=some_func, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()
print(some_var)
