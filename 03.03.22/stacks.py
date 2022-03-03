a = []

a.append(5)
print(a.pop())

from collections import deque

a = deque()

a.append(6)
a.pop()

from queue import LifoQueue

a = LifoQueue()

a.put(5)
a.get()
