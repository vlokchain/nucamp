def linear_search(dictionary, target):
    for x in dictionary.keys():
        if target == dictionary[x]:
            print("Found at the key", x) 
            return x
    else:
        print("Target is not in the dictionary") 
    return -1

dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search(dictionary, 5)
linear_search(dictionary, 3)
linear_search(dictionary, 8)

"""
OUTPUT:
Found at index 4
Found at index 1
Target is not in the list
"""