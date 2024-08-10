from multiprocessing import Process, freeze_support
import os
import time

def my_fun():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == '__main__':
    freeze_support()  # Required for Windows
    process = []
    process_count = os.cpu_count()

    # Create processes
    for pro in range(process_count):
        p = Process(target=my_fun)
        process.append(p)

    # Start processes
    for p in process:
        p.start()

    # Join processes
    for p in process:
        p.join()

    print("End main")
