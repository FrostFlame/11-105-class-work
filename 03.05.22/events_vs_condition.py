from threading import Event, Thread, Condition

# event = Event()
event = Condition()

def worker(name):
    while True:
        event.acquire()
        event.wait()
        print(f'worker: {name}')
        event.release()

# event.clear()
workers = [Thread(target=worker, args=(i,)) for i in range(5)]

for w in workers:
    w.start()

print('Main thread')

# event.set()
while True:
    event.acquire()
    event.notify_all()
    event.release()
