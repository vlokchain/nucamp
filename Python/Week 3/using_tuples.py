# TUPLES: like lists, ordered sequence of multiple values (immutable/cannot be changed)

"""
1. Values can be any data type
2. Values can be duplicate values
3. Parenthesis are optional but recommended
4. Contents are zero-indexed
5. Can use stadard bracket notation to retrieve values
6. More efficient than lists because memory does not need to be dynamically allocated
"""

# VALUES CAN BE UPDATED
animals = ("ape", "zebra", "penguin")
animals = ("elk", "zebra", "penguin")

# VALUE CANNOT BE REASSIGNED
animals[0] = "lion"                    # not allowed
animals.pop(1)                         # not allowed

# ITERATING
tuple = (1, 2, 3, 4, 5)

print(tuple[0] + tuple[1])             # OUTPUT = 3

print(tuple[-1] + tuple[-2])           # OUTPUT = 9

total = 0
for n in tuple:
    total += n
print(total)                           # OUTPUT = 15