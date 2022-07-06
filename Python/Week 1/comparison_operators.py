# COMPARISON OPERATORS are boolean and evaluate as True or False

x = 100
y = 200

print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= y)   # False
print(x <= y)   # True

# LOGICAL OPERATORS
# and = both sub-expressions must be true for compound expression to be true
# or  = either sub-expression must be true for compound expression to be true
# not = if expression is true, it returns false + if expression is false, it returns true

x = 100
y = 200
z = 100

print (x < y and y > z)   
print(x > y or y > z)
print(not(x > y or y > z))
