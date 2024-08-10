from multiprocessing import Process, Lock, Queue


def add_number(number, q):
    for i in number:
        q.put(i+i)


def mul_number(number, q):
    for i in number:
        q.put(i*i)


if __name__ == '__main__':
    q = Queue()
    number = range(1, 6)
    p1 = Process(target=add_number, args=(number, q))
    p2 = Process(target=mul_number, args=(number, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
