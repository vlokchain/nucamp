# DECLARING VARIABLES

x = 12.2
y = 7
z = 9.0

print(x)
print(y)
print(z)

"""
RESULT

newdev@Lenovo-Alt MINGW64 ~/Desktop/NucampFolder/Python/1-Fundamentals/week1
$ python data_types.py
12.2
7
9.0
"""

# PRIMITIVE DATA TYPES

name = "Bob"           # Storing a Sting value
age = 35               # Storing an Integer value
cash = 100.25          # Storing a Float value
retired = False        # Storing a Boolean value

# How to know the data type of a variable: type((variable_name)
print("Data Type of the varibale 'name' is", type(name))
print("Data Type of the varibale 'age' is", type(age))
print("Data Type of the varibale 'cash' is", type(cash))
print("Data Type of the varibale 'retired' is", type(retired))

# COMPOSITE DATA TYPES
# LIST = ordered sequence of multiple values and are mutable (can be changed)
"""
1. You can indent a list within a list
2. List index: first item index starts at 0, second item index starts at 1
3. print(nucamp_locations[1]) = Tacoma
"""
numcamp_locations = ["Seattle", "Tacoma", "Bellevue"]

# DICTIONARY = Ordered collection of key-value pairs (mutable)
"""
1. Can be empty
2. Keys must be unique, duplicate keys will overwrite (second duplicate entry will replace first original entry)
3. Values do not need to be unique and can be changed
3. Can be any immutable data type: itegers, floats, strings, boolean
4. Keys are used as indexes to access values using braket notation
"""
Bob_Info = {"name": "Bob", "age": 35, "cash": 100.25, "retired": False}

# TUPLE = Similar to list but immutable (cannot be changed)
"""

"""
my_tuple = ("apple", "banana", "cherry")

# SET = unordered collection of immutable (cannot be changed) unique values
my_set = {"cats", "dogs", "birds"}

print("Data Type of the varibale 'numcamp_locations' is", type(numcamp_locations))
print("Data Type of the varibale 'Bob_Info' is", type(Bob_Info))
print("Data Type of the varibale 'my_tuple' is", type(my_tuple))
print("Data Type of the varibale 'my_set' is", type(my_set))

"""
TERMINAL RESULT =

newdev@Lenovo-Alt MINGW64 ~/Desktop/NucampFolder/Python/1-Fundamentals/week1
$ python data_types.py
12.2
7
9.0
Data Type of the varibale 'name' is <class 'str'>
Data Type of the varibale 'age' is <class 'int'>
Data Type of the varibale 'cash' is <class 'float'>
Data Type of the varibale 'retired' is <class 'bool'>
Data Type of the varibale 'numcamp_locations' is <class 'list'>
Data Type of the varibale 'Bob_Info' is <class 'dict'>
Data Type of the varibale 'my_tuple' is <class 'tuple'>
Data Type of the varibale 'my_set' is <class 'set'>

"""

#END