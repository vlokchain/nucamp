# WHAT IS A LINKED LIST?
"""
1. A linked list is an abstract data type optimized for quick insertion and deletion by storing data in sequential order
2. A linked list has an order but is not indexed
3. It is ordered using links from node to node
"""

# WHAT IS A NODE?
"""
1. A node consists of two parts called: |value| and |next|
2. |value| is some data that's stored in the current node
3. |next| is a reference to the next node's memory address
4. You can't start in the middle or go backwards you have to start with the first location then you go to the second location
5. In a linked list you start at the head which gives you a value and directions to the next node.
6. When you reach a node that has a |null| value for its next instead of its memory address that's the end of the list
"""

# LINKED LIST VS INDEXED (PYTHON) LIST
"""
1. A linked list does not have an index, you must go grom 1st ndoe to 2nd node to 3rd node to 4th node and so on
2. Each node only has information about the next node in the linked chain
3. Data Retrieval: use a python list rather than linked list when accessing/retriving multiple items
4. Inserting and Deleting Data: use a linked list to quickly insert/delete items. when using a python lists the index will shift  for every item after the insert/delete point.
5. Inserting/deleting with a linked list is a breeze all we need to do is change the next reference point for the two affected nodes
"""