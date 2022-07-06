# A STRING IS IMMUTABLE (CANNOT BE CHANGED)

my_string = "alpha"

# MULTI-LINE STRING
multiline_string = """
bravo
charlie
delta
"""
print(my_string)           # OUTPUT = alpha
print(multiline_string)    # OUTPUT = bravo charlie delta

print(my_string[0])        # OUTPUT = a
print(my_string[:2])       # OUTPUT = al
print(my_string[2:])       # OUTPUT = pha

# ITERATING A STRING USING |for|

for x in my_string:
    print(x)            # OUTPUT = a l p h a

# THE |in| KEYWORD

print("pha" in my_string)
print("z" not in my_string)
