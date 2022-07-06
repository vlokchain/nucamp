# BASIC IMPLEMENTATION OF A LINKED LIST:

class Node:
    def __init__(self, value):     # Constructor method with parameters |self| and |value|
        self.value = value         # We will initialize the value of each node object with a value that will be passed when the node is created
        self.next = None           # The next attribute will initialize in the constructor to |none|. It is a special value in python that denotes the lack of any value.

head = Node("1st Node")            # Instantiating the first node object and setting it = a variable |head|
head.next = Node("2nd Node")       # |head.next| refers to the next attribute of the node we just created
head.next.next = Node("3rd Node")  # |head.next.next| refers to the next attribute of the node we just created

print(head.value)                  # How to access values stored in the 1st node
print(head.next.value)             # How to access values stored in the 2nd node
print(head.next.next.value)        # How to access values stored in the 3rd node


