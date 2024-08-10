#collections: Counter, namedtuple, OrderDict, defaultdict, deque
from collections import Counter, namedtuple, defaultdict, deque

#Counter
a = "aaaaabbbbbcccccffff"
my_counter = Counter(a)
print(my_counter) #Counter({'a': 5, 'b': 5, 'c': 5, 'f': 4})

# access items and keys, values
print(my_counter.items()) #dict_items([('a', 5), ('b', 5), ('c', 5), ('f', 4)])
print(my_counter.keys())  #dict_keys(['a', 'b', 'c', 'f'])
print(my_counter.values())  #dict_keys(['a', 'b', 'c', 'f'])

#check most common element
print(my_counter.most_common(1)) # only 1 most common [('a', 5)]
#access element
print(my_counter.most_common(1)[0][0]) #output: a

print(my_counter.most_common(2)) # only 2 most common [('a', 5), ('b', 5)]

#element
my_element = my_counter.elements()
print(list(my_element)) #['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'f', 'f', 'f', 'f']


#namedtuple: used to create light weight class object
"""namedtuple is a function in the collections module in Python that allows you to create tuple subclasses with named fields.
This provides a way to access elements of the tuple using named attributes,
making the code more readable and self-documenting."""

Point = namedtuple("Point", 'x y')
my_instance = Point(1, 2)
print(my_instance)
print(my_instance.x)
print(my_instance.y)

# Define the namedtuple
Person = namedtuple('Person', ['name', 'age', 'gender'])

# Create an instance of the namedtuple
person1 = Person(name='Alice', age=30, gender='Female')

# Access the fields
print(person1.name)   # Output: Alice
print(person1.age)    # Output: 30
print(person1.gender) # Output: Female

# Namedtuples are still tuples
print(person1[0])  # Output: Alice
print(person1[1])  # Output: 30s
print(person1[2])  # Output: Female

# Example with Default Values:

# Define the namedtuple with default values
Person = namedtuple('Person', ['name', 'age', 'gender'])
Person.__new__.__defaults__ = ('Unknown', 0, 'Unknown')

# Create an instance with some default values
person2 = Person(name='Bob')

print(person2.name)   # Output: Bob
print(person2.age)    # Output: 0
print(person2.gender) # Output: Unknown

# Use Cases
"""
Namedtuples are particularly useful in situations where you want to return multiple values from a function and access them by name, rather than by index.
They are also helpful in making code more readable and maintaining a clear structure in data handling.
"""
# Define the namedtuple
Point = namedtuple('Point', ['x', 'y'])

def create_point(x, y):
    return Point(x, y)

# Use the namedtuple
p = create_point(3, 4)
print(p.x)  # Output: 3
print(p.y)  # Output: 4


# Yes, you can define methods in a namedtuple just like in a regular class. This can be achieved by subclassing the namedtuple. Here’s how you can do it:
#
# First, create the namedtuple using the namedtuple factory function.
# Subclass the namedtuple and define methods in the subclass.


# Step 1: Create the namedtuple
Person = namedtuple('Person', ['name', 'age', 'gender'])

# Step 2: Subclass the namedtuple and add methods
class PersonWithMethods(Person):
    def greet(self):
        return f"Hello, my name is {self.name}."

    def is_adult(self):
        return self.age >= 18

# Create an instance of the subclassed namedtuple
person1 = PersonWithMethods(name='Alice', age=30, gender='Female')

# Access fields
print(person1.name)  # Output: Alice

# Call methods
print(person1.greet())      # Output: Hello, my name is Alice.
print(person1.is_adult())   # Output: True


import csv

# Define the namedtuple
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

# Open and read the CSV file
with open("employees.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for emp in map(EmployeeRecord._make, reader):
        print(f"{emp.name}: {emp.title}")


NewNum1 = namedtuple("NewNum", "x, y")
NewNum2 = namedtuple("NewNum", ["x", "y"])


t = [11, 22]
j = NewNum1._make(t)
j1 = NewNum2._make(t)
print(j)
print(j1)
# Return a new dict which maps field names to their corresponding values:
print(j1._asdict())

# To convert a dictionary to a named tuple, use the double-star-operator (as described in Unpacking Argument Lists):
d = {'x': 11, 'y': 22}
out = Point(**d)
print(out)


#defaultdict
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])


# Create a defaultdict with a default type of list
dd = defaultdict(list)

# Accessing a non-existent key returns a default value (an empty list in this case)
print(dd['missing'])  # Output: []

# Modifying the default value
dd['missing'].append(1)
print(dd['missing'])  # Output: [1]

# defaultdict with set

# Create a defaultdict with a default type of set
dd = defaultdict(set)

# Adding to the set of a non-existent key
dd['animals'].add('cat')
dd['animals'].add('dog')
print(dd['animals'])  # Output: {'cat', 'dog'}


# Example Use Case: Counting Word Frequencies
# Here is an example where defaultdict is used to count the frequency of words in a text:
# Sample text
text = "apple banana apple orange banana apple"

# Create a defaultdict with a default type of int
word_count = defaultdict(int)

# Split the text into words and count the frequencies
for word in text.split():
    word_count[word] += 1

# Print the word frequencies
print(word_count)

#deque
"""
deque (pronounced "deck") is a double-ended queue provided by the collections module in Python.
It allows you to add and remove elements from both ends with O(1) performance.
deque is useful for implementing queues, stacks, and other data structures where you need efficient append and pop operations from both ends.
"""
d = deque('ghi') # make a new deque with three items

# iterate over the deque's elements
for elem in d:
    print(elem.upper())

# add a new entry to the right side
d.append("f")
print(d)
# add a new entry to the left side
d.appendleft("i")
print(d)

 # return and remove the rightmost item
elem = d.pop()
print(elem)
# return and remove the leftmost item
elem = d.popleft()
print(elem)
print(d)
 # list the contents of the deque
d_list = list(d)
print(d_list)
# peek at leftmost item
print(d_list[0])
# peek at rightmost item
print(d_list[-1])

# list the contents of a deque in reverse
print(list(reversed(d_list)))

 # search the deque
is_present = "h" in d_list
print(is_present)

# add multiple elements at once
d_list.extend("kjl")
print(d_list)

# right rotation
d = deque(d_list)
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
 # make a new deque in reverse order
d.clear()
print(d)
# extendleft() reverses the input order
d.extendleft('abc')
print(d)
