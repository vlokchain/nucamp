# FOR LOOP CONTROL USE THE LOOP CONTROL STATEMENTS: BREAK + CONTINUE

# BREAK LOOP CONTROL STATEMENT: stops entire for loop

for x in "string":
    if x == "i":
        break
    print(x)

    """
    OUTPUT:
    s t r
    """

# CONTINUE LOOP CONTROL STATEMENT: only stops current iteration of the for loop

for x in "string": 
    if x == "i":
        continue  # SKIPS "i"
    print(x)

    """
    s t r n g
    """