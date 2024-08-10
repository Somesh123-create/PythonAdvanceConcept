from multiprocessing import Process, Value, Array, Lock
import os
import time

def add_number(number, lock):
    with lock:
        for i in range(100):
            time.sleep(0.1)
            number.value += 1


def add_array_val(number, lock):
        for i in range(100):
            with lock:
                for i in range(len(number)):
                    number[i] += 1


if __name__ == '__main__':
    # how to use Value
    lock = Lock()
    shared_val = Value('i', 0)
    print("Number at beginning is:", shared_val.value)
    p1 = Process(target=add_number, args=(shared_val,lock))
    p2 = Process(target=add_number, args=(shared_val,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Number at end is:", shared_val.value)

    #how to use Array
    lock = Lock()
    shared_arry = Array('d', [0.0, 100.0, 200.0])
    print("Arry at beginning is:", shared_arry[:])

    p1 = Process(target=add_array_val, args=(shared_arry,lock))
    p2 = Process(target=add_array_val, args=(shared_arry,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Arry at end is:", shared_arry[:])
