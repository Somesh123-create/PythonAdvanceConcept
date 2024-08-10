from threading import Thread, Lock
import time

data_val = 0

def increase(lock):
    lock.acquire()
    global data_val
    copy_local = data_val
    copy_local += 1
    time.sleep(0.1)
    data_val = copy_local
    lock.release()

#using lock context
def increase_con(lock):
    with lock:
        global data_val
        copy_local = data_val
        copy_local += 1
        time.sleep(0.1)
        data_val = copy_local


if __name__ == '__main__':
    lock = Lock()
    print("before start:", data_val)
    thread1 = Thread(target=increase_con, args=(lock,))
    thread2 = Thread(target=increase_con, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("after end:", data_val)
