# LAMBDA FUNCTION SYNTAX

"""
1. Similar to arrow functions in JavaScript
2. Known as anonymous functions (technically do not have a name)
3. Used in special situations when a function does not need a name or held in memory for later use"""

# SYNTAX
"""
1. Argument list is comma-seperated
2. Multiple arguments allowed
3. Only one expression/line allowed in function body
"""

# lambda arg1, arg2: expression to return

# EXAMPLE:

lambda num: num ** 2

# is the same as:

def square(num):
    return num ** 2

# CALLBACK FUNCTIONS: are functions used by high-order functions as arguments
# Note: functions can be used as arguments for other functions
# Note: high-order functions are functions that use other functions as arguments

# EXAMPLE:

def a_function(callback):           # this high order function has a parameter of a callback function
    print(callback(3))

a_function(lambda num: num ** 2)    # this calls the higher-order function with a lambda function argument
