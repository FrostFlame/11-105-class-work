from threading import Semaphore, Thread
from time import time, sleep

ticket_office = Semaphore(3)


def ticket_buyer(number):
    start_service = time()
    with ticket_office:
        sleep(1)
        print(f'client {number}, service time: {time() - start_service}')


buyer = [Thread(target=ticket_buyer, args=(i,)) for i in range(5)]

for b in buyer:
    b.start()
