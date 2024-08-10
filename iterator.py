#itertools: product, permutations, combinations, combinations_with_replacement, accumulate, groupby and Infinite iterators
#Functions creating iterators for efficient looping
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator
# product
# cartesian product, equivalent to a nested for-loop

a = [1, 2]
b = [3, 4]

prod = product(a, b)
print(list(prod))

#repeat Infinite iterators
# prod = product(a, b, repeat=2)
# print(list(prod))

# permutations
# all possible orderings, no repeated elements
a = [1, 2, 3]
perm1 = permutations(a)
perm2 = permutations(a, r=2)
print(list(perm1))
print(list(perm2))

#combinations
# r-length tuples, in sorted order, no repeated elements
a = [1, 2, 3, 4]
comb2 = combinations(a, r=2)
comb3 = combinations(a, r=3)
print(list(comb2))
print(list(comb3))

# combinations_with_replacement
# r-length tuples, in sorted order, with repeated elements
a = [1, 2, 3, 4]
comb_repl2 = combinations_with_replacement(a, r=2)
comb_repl3 = combinations_with_replacement(a, r=3)
print(list(comb_repl2))
print(list(comb_repl3))

#accumulate
# Make an iterator that returns accumulated sums or accumulated results from other binary functions.
# p0, p0+p1, p0+p1+p2,
# accumulate([1,2,3,4,5]) → 1 3 6 10 15
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

#using operator

acc_mul = accumulate(a, func=operator.mul)
print(a)
print(list(acc_mul))


a = [1, 2, 5, 3, 4]
acc_max = accumulate(a, func=max)
print(a)
print(list(acc_max))

# groupby
# sub-iterators grouped by value of key(v)
# Sample data
data = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]
# Grouping the data
grouped_data = groupby(data)

# Printing the groups
for key, group in grouped_data:
    print(f"Key: {key}, Group: {list(group)}")

# Using groupby with a Key Function
# You can also provide a key function to groupby to specify how the elements should be grouped. Here’s an example where we group words by their first letter:

#groupby 1st later of world
def fun_w(x):
    return x[0]

#groupby world
def fun_w(x):
    return x


words = ["apple", "apricot", "banana", "berry", "cherry", "apple", "cranberry", "date"]

#before apply group make sure sort it
words.sort()

grouped_word = groupby(words, key=fun_w)
for k, v in grouped_word:
    print(k, list(v))


#how to use lambda func

grouped_word = groupby(words, key=lambda x: x[0])
for k, v in grouped_word:
    print(k, list(v))


grouped_word = groupby(words, key=lambda x: x)
for k, v in grouped_word:
    print(k, list(v))


# Sample data
data = [
    {"name": "Alice", "department": "Engineering"},
    {"name": "Bob", "department": "Engineering"},
    {"name": "Charlie", "department": "HR"},
    {"name": "Diana", "department": "HR"},
    {"name": "Eve", "department": "Marketing"}
]


data.sort(key=lambda x: x["department"])

dp_group = groupby(data, key=lambda x: x["department"])

for k, v in dp_group:
    print(k, list(v))


# count, cycle, repeat (Infinite iterators)
for i in count(5):
    print(i)
    if i == 100:
        break

a = [1, 2, 3]
count = 0
for i in cycle(a):
    print(i)
    count += 1
    if count > 50:
        break

for i in repeat(3, 5):
    print(i)
