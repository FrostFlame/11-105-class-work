from threading import Event, Thread

event = Event()


def worker(name):
    event.wait()
    print(f'worker: {name}')


event.clear()
workers = [Thread(target=worker, args=(i,)) for i in range(5)]

for w in workers:
    w.start()

print('Main thread')

event.set()
