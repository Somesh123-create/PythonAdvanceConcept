my_list = ["hello", 12, "raj", 10.5]

"""
List Methods:
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

"""

# append
my_list.append("somesh")
#print(my_list)

# clear
my_list.clear()
#print(my_list)


# copy
my_list.append("anoop")
new_list = my_list.copy()
#print(new_list)


# count
new_list.append("anoop")
#print(new_list.count("anoop"))


#extend
new_list.extend([1, 3, 5, 4])
#print(new_list)


#index
value_index = new_list.index(3)
#print(value_index)

#insert -> take 1st arg as index and 2nd args replacement value

new_list.insert(2, 0)
# print(new_list)

#pop  -> takes index as args
# print("Before list:",new_list)
new_list.pop()
new_list.pop(1)
# print("After list:",new_list)

#remove -> takes one aregs as value to be remove

# print(new_list)
new_list.remove(0)
# print(new_list)

#reverse

print(new_list)
#sort
