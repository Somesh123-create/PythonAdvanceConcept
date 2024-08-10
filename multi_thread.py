from threading import Thread
import time

threads = []
thread_count = 10


def my_fun():
    for i in range(100):
        i * i
        time.sleep(0.1)

#create threads
for i in range(thread_count):
    t = Thread(target=my_fun)
    threads.append(t)

#start threads
for t in threads:
    t.start()

#join threads
for t in threads:
    t.join()

print("Finished")
