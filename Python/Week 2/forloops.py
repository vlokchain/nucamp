# FOR LOOPS WITH RANGE FUNCTION

"""
Used to repeat a code block a fixed number of times.
range() is used to define the fixed number.
"""

for i in range (0, 5, 1):  # Will stop at 4
    print(i)

"""
OUTPUT:
0 1 2 3 4
"""

# THE SYNTAX

"""
for <iteration variable> in range (start, stop, step):
    statement 1
    statement 2

breakdown:

start = initial start value of i
stop  = max value of i
step = increment/decremt of i
"""

# FOR LOOPS WITH ITERABLE VALUE

"""
Another way to define a fixed number of times is by providing the for loop with an iterable value.

This can include: Lists, Tuples, Dictionary, Set or a String.

A for loop with iterable value can step through the contents of the value such as the items inside a:

List or
The characters in a string or
Keys in dictionary.

Then when we've stepped through all the items at the end of the list the for loop stops.
"""

# EXAMPLE

for x in "string":
    print(x)

    """
    OUTPUT:
    s t r i n g
    """