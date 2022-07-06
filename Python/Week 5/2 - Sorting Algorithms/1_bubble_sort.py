# Implement the bubble sort algorithm, using a Python list and nested for loops.

unsorted_list = [101, 49, 3, 12, 56]  # An unsorted list with an index = 4 and length = 5

def bubblesort(the_list):
    high_idx = len(the_list) - 1       # The highest index = to length of the list -1. The decrement is used to shift legnth of list to the index value of the list.

    for i in range(high_idx):          # i starts at = 0, stops/exits loop when i = to 4, increments i by 1: A |for| loop with i as the iterating variable to bubble sort the |unsorted_list|
        list_changed = False           # Add boolean values to detect changes in list: |for| loop will loop until it reaches maximum number of loops even if list is fully sorted: add a Boolean value of |False| to fix this
        for j in range(high_idx):      # A second nested |for| loop with j as the iterating variable is used as thr first step to create the adjacent pair for the i |for| loop 
            item = the_list[j]         # Creating adjacent pair step 3: a variable set = to the list with the |i| variable = to index 0
            next = the_list[j+1]       # Creating adjacent pair final step: a variable set = to the list with the |j| varialbe = to the index 0 + 1 so index = 1

                                       # |item| and |next| represent the pair in the bubble sort being sorted

            if item > next:            # |if| statement to begin the sorting process by comparing if the variable = |item| is greater than the varaible = |next|
                the_list[j] = next     # Statement #1 to swap variables/begin sort when if condition is met: the values will reverse for the varaibles from the |for| loop. |next| is now set to the value of |item| value
                the_list[j+1] = item   # Statement #1 to swap variables/begin sort when if condition is met: the values will reverse for the varaibles from the |for| loop. |item| is now set to the value of |next| value
                list_changed = True    # If the lists changes and we end up in the |if| statement add Boolean value of = to |True|
            print(the_list, i, j)      # Prints contents of the list and the iterations of then |i| and |j|
        print(list_changed)            # Prints True or False for testing/visual purposes after |i| and |j| complete one full interation of the indeces
        if list_changed == False:      # Takes point from Line 7 and 17 to detect changes in the list and exit the for loop once the list stops changing is done being sorted by breaking out of the for loop
            break

bubblesort(unsorted_list)              # Testing |bubblesort| function