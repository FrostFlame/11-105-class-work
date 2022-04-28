from threading import Thread
from time import sleep


def func(n):
    for i in range(n):
        print(f'from child thread: {i}')
        sleep(0.5)


# class MyThread(Thread):
#     def __init__(self, n):
#         super().__init__()
#         self.n = n
#
#     def run(self):
#         for i in range(self.n):
#             print(f'from child thread: {i}')
#             sleep(0.5)

# func()

# th = Thread(target=func, args=(5,))
# th1 = MyThread(5)
# th2 = MyThread(10)
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()

# print('End of main thread')


th = Thread(target=func, args=(5,))
print(f"thread status: {th.is_alive()}")

th.start()
print(f"thread status: {th.is_alive()}")

sleep(5)
print(f"thread status: {th.is_alive()}")