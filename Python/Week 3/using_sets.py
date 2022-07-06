# SETS = Unordered collection of values

"""
1. Cannot be indexed by bracket notation
2. Is mutable but cannot have mutable data types
3. Items must have unique values
4. Duplicates are removed
"""

# CREATE EMPTY SET
empty_set = set()

# DUPLICATE VALUES ARE REMOVED
numbers_set = {1, 2, 3, 4, 4}
print(numbers_set)                             # OUTPUT  = {1, 2, 3, 4}

# CANNOT USE MUTABLE DATA TYPES
numbers_set = {1, 2, 3, 4, [5, 6]}             # not allowed: [5, 6] is a list and a mutable data tyoe

# TUPLES CAN BE USED
numbers_set = {1, 2, 3, 4, (5, 6)}             # allowed: tuples are immutable, OK to use!

# ITERATING 1
words_set = {"Alpha", "Bravo", "Charlie"}
abcd = ""
for word in words_set:
    abcd += word
print(abcd)                                    # OUTPUT  = AlphaBravoCharlie or BravoCharlieAlpha or CharlieBravoAlpha, values are unordered

# ITERATING 2
if "Alpha" in words_set:
    print("Alpha is in set")
else:
    print("Alpha not in set")                  # OUTPUT = Alpha is in set

# MODIFYING SET VALUES
words_set.add("Delta")                         # adds a new value to set
print(words_set)                               # OUTPUT = {"Alpha", "Bravo", "Charlie", "Delta"}

words_set.discard("Bravo")                     # discards a value from set
print(words_set)                               # OUTPUT = {"Alpha", "Charlie", "Delta"}