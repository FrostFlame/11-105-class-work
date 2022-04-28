from threading import Timer
from time import sleep

timer = Timer(interval=3, function=lambda: print("Message from Timer!"))
timer.start()

for i in range(5):
    print('asdsadada')
    sleep(1)
