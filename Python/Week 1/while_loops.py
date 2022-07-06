# WHILE LOOP

n = 5
while n > 0:
    print(n)
    n = n - 1
print("blastoff!")
print(n)

"""
OUTPUT: 5 4 3 2 1 blastoff! 0
"""

# BREAK STATEMENT: stops the loop even if while condition is true

n = 5
while n > 1:
    print(n)
    n = n - 1
    if n == 2:
        break
print(n)

"""
OUTPUT: 5 4 3 2
"""

# CONTINUE STATEMENT: stops current iteration and continues with next statement

n = 5
while n > 1:
    n = n - 1
    if n == 2:
        continue
    print(n)

"""
OUTPUT: 4 2 1
"""