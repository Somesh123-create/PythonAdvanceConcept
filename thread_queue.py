from threading import Thread, Lock, current_thread
from queue import Queue
import time



def my_fun(locks, q):
    while True:
        value = q.get()
        with locks:
            print(f"we are in thread: {current_thread().name} and value is: {value}")
            print(value)
        q.task_done()

if __name__ == '__main__':
    lock = Lock()
    q = Queue()
    num_thread = 10

    for i in range(num_thread):
        thread1 = Thread(target=my_fun, args=(lock, q))
        thread1.daemon = True
        thread1.start()

    for j in range(1, 25):
        q.put(j)

    q.join()
    print("Done")
