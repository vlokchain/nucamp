# CHAINING AND NESTING CONDITIONS

# Can have nested |if| statements (avoid and use logical operators)

x = 100
if x > 1:
    print("More than one")
    if x < 100:
        print("Less than 100")

# Can only have one |else| statement at the end 
# Can have as many |elif| staments in between 

y = 50
if y < 5:
    print("xs small")
elif y < 10:
    print("small")
elif y < 20:
    print("medium")
else:
    print ("Large")

# Avoid nested |if| statements and use logical operators

z = 50

if z < 10 and z < 100:
    print("More than one")
    print("Less than 100")
print ("All done")