# DICTIONARY = Ordered collection of key-value pairs (mutable)

"""
1. Can be empty
2. Keys must be unique, duplicate keys will overwrite (second duplicate entry will replace first original entry)
3. Values do not need to be unique and can be changed
3. Can be any immutable data type: itegers, floats, strings, boolean
4. Keys are used as indexes to access values using braket notation
"""

state_capitals = {"washington": "olympia", "oregon": "salem", "california": "sacramento"}

print(len(state_capitals))                       # OUTPUT = 3

print(state_capitals["washington"])              # OUTPUT = olympia

# MODIFYING VALUE OF A KEY
state_capitals["washington"] = "aberdeen"        # changes the value for the "washington" key
print(state_capitals)                            # OUTPUT = {"washington": "aberdeen", "oregon": "salem", "california": "sacramento"}


# ADDING NEW KEY VALUE
state_capitals["texas"] = "austin"               # adds new key value pair to end of dictionary 
print(state_capitals)                            # OUTPUT {"washington": "aberdeen", "oregon": "salem", "california": "sacramento", "texas": "austin"}

# REMOVING KEY VALUE: using |del| = does not store return value or |pop| = pop is a method and stores return value
del state_capitals["california"]                 # deletes specified key value without storing return value
print(state_capitals)                            # OUTPUT = {"washington": "aberdeen", "oregon": "salem", "california", "texas": "austin"}

state_capitals.pop("oregon")                     # deletes specified key value and stores return value
print(state_capitals)                            # {"washington": "aberdeen", "california", "texas": "austin"}

removed_capital = state_capitals.pop("oregon")   # pop method is set as variable |removed_capital|
print(state_capitals)                            # prints the now |state_capitals|
print(removed_capital)                           # OUTPUT = salem, returns the deleted capital

# USING |for| + |in| LOOPS

state_capitals = {"washington": "olympia", "oregon": "salem", "california": "sacramento"}

for state in state_capitals:
    print(state)                               # OUTPUT =  washington oregon california, prints the keys

for city in state_capitals.values():             # OUTPUT = olympia salem sacramento, prints the values
    print(city)

for x, y in state_capitals.items():
    print(y, "is the capital of", x) 

"""
OUTPUT:
olympia is the capital of washington
salem is the capital of oregon
sacramento is the capital of california
"""
