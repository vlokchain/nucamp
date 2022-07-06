"""
1. Not all python functionality is laoded by default.
2. There are dozens of built-in-modules that can be imported.
3. There are about 24 methods in the |random| module
4. To use methods from the |random| module in a python file use |import random| at the top of your file
"""

# randint()
# RETURNS RANDOM INTEGER FROM MIN+MAX ARGUMENT

import random

random.randint(11, 15) 

"""
A. 1st argument = 11 = minimum integer
B. 2nd argument = 15 = maximum integer
C. returns = randim integer between 11 and 15, inclusive
D. outcome can be = 11 or 12 or 13 or 15
"""

# choice()
# RETURNS RANDOM VALUE FROM SEQUENCE DATA TYPE

pets = ["bird", "dog", "turtle", "cat"]
random.choice(pets)

"""
outcome can be = "bird" or "dog" or "turtle" or "cat"
"""

# shuffle()
# RETURNS A SHUFFLED LIST

pets = ["bird", "dog", "turtle", "cat"]
random.shuffle(pets)