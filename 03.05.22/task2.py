from threading import Semaphore, Thread
from time import time, sleep


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f'{self.value} с приоритетом {self.priority}'


my_list = [Node(i, pr) for i, pr in zip(range(10), [1, 2, 3, 1, 1, 2, 1, 3, 2, 2])]

semaphore = Semaphore(3)


def foo(node):
    start = time()
    with semaphore:
        sleep(1)
        print(f'Обработана нода {node} за {time() - start}')


workers = [Thread(target=foo, args=(node,)) for pr_list in
           [(lambda x: list(filter(lambda x: x.priority == pr, x)))(my_list) for pr in range(3, 0, -1)] for node in
           pr_list]
for w in workers:
    w.start()
