# Implement the linear search algorithm to search through a Python List data structure:

"""
Let's define a function called linear_search this function will use parameters of a list let's give it a name to use within
the function of the underscore list and a target value to search for in the list
"""

def linear_search(the_list, target):   # Defined a function |linear_search| with parameters of a list this function will use parameters of a list |the_list| and |target| value to search for in the list
    for x in range(len(the_list)):     # range(0, len(the_list), 1):This will take the length of |the list| that is how many items are in it and use it with the range function to iterate that many times. When one argument provided in rage it is used as the stop value. Then the start becomes = 0 and step = 1. Will start with x set to 0 then iterate as many times as there are items in the list and value of x will increment by 1 each time
        if the_list[x] == target:      # If the list item at the |x| index = to the |target|
            print("Found at index", x) # If it is it will print  
            return x                   # and it returns x
    print("Target is not in the list") # If it is not it will print 
    return -1                          # and it returns -1 because the index for a list must always be 0 or higer

my_list = [6, 3, 4, 2, 5, 7]           # Testing linear search function with a list
linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 8)

"""
OUTPUT:
Found at index 4
Found at index 1
Target is not in the list
"""