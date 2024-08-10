import sys

def my_fun(n):
    num = []
    count = 0
    while count < n:
        num.append(count)
        count += 1
    return num


def my_generator(n):
    nums = 0
    while nums < n:
        yield nums
        nums += 1

f = my_fun(10)
print(f)

g = my_generator(10)
print(list(g))
print(sys.getsizeof(f))
print(sys.getsizeof(g))


# expression

mygen = (i for i in range(100000) if i %2 ==0)
# print(list(mygen))
print(sys.getsizeof(mygen))

mylist = [i for i in range(100000) if i %2 ==0]
# print(mylist)
print(sys.getsizeof(mylist))
