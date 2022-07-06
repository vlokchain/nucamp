"""
THERE ARE 4 DIFFERENT NON-RELATED PYTHON EXPRESSIONS BELOW
"""

# Code Challenge: For Loop 1

for i in range(20, -20, -5):
    print(i)

# Code Challenge: For Loop 2

for x in range(0, 6, 1):
    if x == 0 or x == 6:
        print("*")
    elif x == 1 or x == 5:
        print("**")
    elif x == 2 or x == 3:
        print("***")
    else:
        print("****")

# Code Challenge: For Loop Loading Bar

for amount_loaded in range(0, 101, 5):
    print(amount_loaded)
    if amount_loaded == 25:
        print("1/4 of the way there")
    elif amount_loaded == 50:
        print("1/2 of the way there")
    elif amount_loaded == 75:
        print("3/4 of the way there")
    elif amount_loaded == 100:
        print("Loading complete")
        break

# Code Challenge: Star Staircase For Loop

stars = ""
for i in range(0, 5, 1):
    for j in range(0, i, 1):
        stars += "*"
    print(stars)
