from multiprocessing import Pool

def cude(number):
    return number * number * number


if __name__ == '__main__':
    number = range(10)
    pool = Pool()

    #map, apply, join, close
    result = pool.map(cude, number)
    pool.close()
    pool.join()
    print(result)
