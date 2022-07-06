# LIST = ordered sequence of multiple values and are mutable (can be changed)

"""
1. You can indent a list within a list
2. List index: first item index starts at 0, second item index starts at 1
"""
states = ["Washington", "Oregon", "California"]

print(states[0]) # = Washington
print(states[1]) # = Oregon
print(states[2]) # = California

print(states[-1]) # = California
print(states[-2]) # = Oregon
print(states[-3]) # = Washington

states[2] = "Arizona"       # Replaces list index 2 or "Oregon" with "Arizona"

print(len(states))          # Returns the length of the list = 3

states.append("New York")   # Adds the appended item to the end of the list

states.pop()                # Removes the last item on a list

states.pop(1)               # Removes the list item index 1

for x in states:            # Output: Washington Oregon California
    print(states)

for states in states:       # Output: Washington Oregon California
    print(states)

for state in states:       # Output: washington oregon california
    state = state.lower()
    print(states)

print("Washington" in states)       # OUTPUT: True
print("Tennessee" in states)        # OUTPUT: False
print("Washington" not in states)   # OUTPUT: False

# CONCATENATING LISTS

states2 = ["Arionza", "ohio", "Louisiana"] # OUTPUT: ["Washington", "Oregon", "California", "Arionza", "Ohio", "Louisiana"]
best_states = states + states2
#print(best_states)""

# SLICING LISTS

print(best_states[1:3])   # OUTPUT: ["Washington", "Oregon", "California", "Arionza", "Ohio", "Louisiana"]
print(best_states[:3])    # OUTPUT: ["Oregon", "California"]
print(best_states[4:])    # OUTPUT: ["Ohio", "Louisiana"]