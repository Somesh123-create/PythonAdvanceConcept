#lambda arguments: expression
from functools import reduce
#single arguments
add10 = lambda x: x+10
print(add10(5))

#multiple arguments
mult = lambda x, y: x * y
print(mult(5, 2))

# using sorted
points2D = [(1, 13), (5, 12), (4, 16), (3, 14)]
points2D_sorted = sorted(points2D) #sorted with x value

print(points2D)
print(points2D_sorted)

#sorted with key lambda
points2D_sorted_key = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted_key)

#sorted by sum of x and y
points2D_sorted_key_sum = sorted(points2D, key=lambda x:x[0] + x[1])
print(points2D)
print(points2D_sorted_key_sum)


#map(func, seq)
a = [2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

#filter(func, seq)
f = [2, 3, 4, 5, 6, 7, 8]
new_val = filter(lambda x: x%2 == 0, f)
print(list(new_val))

#reduce(func, seq)
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x*y, a)
print(b)
