# Set: unordered, mutable, no duplicate
my_sets = {1, 2, 3, 4, 4, 5}
print(my_sets)

#create set by list
myset = set([1, 2, 3])
print(myset)

#create set and removed duplicate from string
myset = set("hello")
print(myset)

#create empty
myset = set()
print(myset)

#add element in Set
myset.add(4)
myset.add(5)
myset.add(6)
print(myset)

#remove element from set
myset.remove(6)
print(myset)

# remove element from discard method if element not found doesnt throw error
myset.discard(4)
print(myset)

# remove element using pop
myset = {1, 2, 3, 4, 5, 6}
print(myset.pop())
print(myset)

# itterate mysets
for i in myset:
    print(i)

# check element present in list
if 6 in myset:
    print("Yes")
else:
    print("no")


#union and intersection, difference, symetric_difference
odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

#union combine both sets
u = odds.union(even)
print(u)

#intersection only print all element found in both sets
i = even.intersection(prime)
print(i)
i = odds.intersection(prime)
print(i)

# difference, its print element from first set those are not in second set
seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 2, 3, 10, 11, 12}

d = seta.difference(setb)
print(d)

d = setb.difference(seta)
print(d)

#symetric_difference: print elements from both sets but not same elements there in both sets
sd = seta.symmetric_difference(setb)
print(sd)

#update sets
seta.update(setb)
print(seta)

# update intersection
seta.intersection_update(setb)
print(seta)

# update difference
seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 2, 3, 10, 11, 12}
seta.difference_update(setb)
print(seta)

#update symetric_difference
seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 2, 3, 10, 11, 12}
seta.symmetric_difference_update(setb)
print(seta)


#issubset and issuperset methods
set_a = {1, 2, 3, 4, 5, 6}
set_b = {1, 2, 3}
set_c = {7, 8}

#check is subset return true when all elements of first sets present in second set

is_subset = set_a.issubset(set_b)
print(is_subset)

is_subset = set_b.issubset(set_a)
print(is_subset)

#check is supersubset: return true when any element from first set present in second set
is_superset = set_b.issuperset(set_a)
print(is_superset)

is_superset = set_a.issuperset(set_b)
print(is_superset)

#isdisjoint: return true not duplicate element found in both sets otherwise false
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)

is_disjoint = set_a.isdisjoint(set_c)
print(is_disjoint)


#frozenset
new_set = frozenset([1, 2, 3, 4])
print(new_set)

# new_set.add(5) #AttributeError: 'frozenset' object has no attribute 'add'
# new_set.remove(3) #AttributeError: 'frozenset' object has no attribute 'remove'
