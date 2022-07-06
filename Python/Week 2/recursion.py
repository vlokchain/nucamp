# RECURSION

"""
1. A function that calls itself is a recursive function
2. Recursive function must have a base condition that will stop the recursion to prevent infinite loops
3. Recursion solves a complex problem by reducing it to simpler versions of the same problem.
"""

# THE FIBONACCI SEQUENCE
# Begins with 0 and 1
# Sum of the two preceding numbers: 0 + 1 = 1, 1 + 2 = 3, 3 + 5 = 8, 5 + 8 = 13

0 | 1 | 1 | 2 | 3 | 5 | 8 | 13
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7    # 0 returns 0, 2 returns 1, 3 returns 3, 4 returns 3, 5 returns 5, 6 returns 8, 7 returns 13 

"""
Write code that takes a number and returns the number at that position in the Fibonacci sequence

Examples:
Given the number 0, returns: 0
Given the number 7, returns: 13
"""

def rFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)

rFib(4)

"""
BREAKDOWN:
1. rFib(4) calls for n = 4 in |def rFib(n)|
2. according to |def rFib(n)| n != 0, 1 or 2 so if and elif blocks are skipped
3. now we move to the final statement |return rFib(n-1) + rFib(n-2)| = rFib(4-1) + rFib(4-2) = rFib(3) + rFib(2)
4. python reads code from L to R so we begin with rFib(3) and go through the statements again, it is not equal to 0, 1 or 2 so we move to final statement
5. rFib(n-1) + rFib(n-2) = rFib(3-1) + rFib(3-2) = rFib(2) + rFib(1) = 1 + 1 = 2
6. now we examine rFib(2) = 1
7. therefore rFib(4) = (rFib(3) + rFib(2)) + rFib(2) = (rFib(2) + rFib(1)) + 1 = (1 + 1) + 1 = 3
"""

# INTERACTIVE PYTHON MODE:

"""
Type: python -i recursion.py 
"""
