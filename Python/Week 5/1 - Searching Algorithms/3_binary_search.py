"""
NOTE: HOW A BINARY SEARCH WORKS:
    1. Find your lower bound
    2. Find your upper bound
    3. Find your pivot: the item in the middle. The pivot is used as the value to compare against the target
    4. Check if pivot value is = to target value: is it closer to lower bound or upper bound?
    5. If target value is higher than pivot value: discard lower values
    6. If target value is lower than pivot value: discard higher values
    7. Repeat steps 3, 4, 5, 6 on non-discarded values until target value is found
"""

def binary_search(the_list, target): # A function w/ parameters |the_list|= a sorted list and |target|= target to search for in list
    lower_bound = 0                  # 1st step: define the lower bound of search interval by index. The search interval is the entire list so we initialize = to 0.
    upper_bound = len(the_list) - 1  # 2nd step: define upper bound of search interval by index. We use |len| to get number if items in list and subtract -1 because |len| of list is total number of items in a list. The decrement will then shift the upper bound to the proper index value of the list.

# Condition for the loop to keep going until we run out of items in the search interval

    while lower_bound <= upper_bound:             # |while| loop will continue to iterate if lower bound is less than or equal to upper bound
        pivot = (lower_bound + upper_bound) // 2  # Pivot value falls between lower and uppper bounds. Mathematically we say: (lower+upper)//2 *use floor division: index do not support float(decimal) value*
        pivot_value = the_list[pivot]             # Compare pivot value against the target values of |the_list| with the |pivot| as the value stored at the index of the list using bracket notation
        if pivot_value == target:                 # If pivot value = to the target |while| loop ends
            return pivot                          # Returns: pivot
        if pivot_value > target:                  # If pivot value greater than target:
            upper_bound = pivot - 1               # Subtract -1 from the upper bound
        else:                                     
            lower_bound = pivot + 1               # Now only option remaining is pivot value is < target so we say: |lower_bound| = |pivot| + 1
    return -1                                     # Return: -1 to signify no index was found carrying target value. If target is not in list than lower bound will eventually be higher than upper bound causing loop to exit without returning a pivot value

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(the_list, 10))
print(binary_search(the_list, 4))
print(binary_search(the_list, 33))