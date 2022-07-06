# SINGLY LINKED LIST: Nodes only have reference to next code and not previous. Can only traverse from Left to Right.

# DOUBLY LINKED LIST: Nodes have reference to next and previous noves. Can traverse from Left to Right and from Right to Left.

class DoubleNode:
    def __init__(self, value):
        self.value = value      # A |self.value| attribute set = |value| data
        self.next = None        # Link to the next node: we don't know what these links are going to be yet so we initialize them to |None|
        self.prev = None        # Link to previous node: we don't know what these links are going to be yet so we initialize them to |None|

class DoublyLinkedList:         # Defining doubly linked list class
    def __init__(self):         # The class constructor will contain the:
        self.head = None        # head node: initialized to |None|  -> when this |DoubleLinkedList| class is instantiated it will not contain any nodes
        self.tail = None        # tail node: initialized to |None|  -> when this |DoubleLinkedList| class is instantiated it will not contain any nodes

    def append(self, value):    # Define an append() method to give this class a way to gain nodes
        new_node = DoubleNode(value)

        if self.head is None:    # Checks if list is empty by checking: |if| |self.head| is |None|. In that case that means our list is empty so |new_node| becoes head and tail nodes.
            self.head = new_node
            self.tail = new_node
            print("head Node created:", self.head.value)
            return

# IMPLEMENTING |prepend| METHOD:
# Write code to handle the append operation: if the list is not empty and there is a head
        new_node.prev = self.tail  # Link previous attribute of |new_node| to the current tail node
        self.tail.next = new_node  # Link next attribute of the current tail to the |new_node|
        self.tail = new_node       # Change reference for |self.tail| to |new_node|
        print("Append new node with value:", self.tail.value)  # Print confirmation message demonstrating the current tail nodes value

dllist = DoublyLinkedList()        # Instantiating an object of the |DoublyLinkedList| class named |dllist|
dllist.append("First Node")        # We will use |append()| method to create a node holding the string value of |"First Node"|

# INTERACTIVE PYTHON FOR DOUBLY LINKED LIST ABOVE:

"""

NOTE: PYTHON INTERACTIVE FOR DOUBLY LINKED LIST SEEN ABOVE:

azurita@A34-009 MINGW64 ~/OneDrive - MetTel/Desktop/Repair/Nucamp
$ python -i doubly_linked_lists.py
head Node created: First Node                                 # Results in the node created from the string value of the first node: dllist.append("First Node")
>>> dllist.head.value                                         # Since |"First Node"| is the only node stored in the list that means it should be stored as both: head and tail node
'First Node'                                                  # Results in the head node
>>> dllist.tail.value                                         # Checks for the tail node
'First Node'                                                  # Results in the tail node
>>> dllist.append("Second Node")                              # Appending a |"Second Node"| by using dllist.append("")
Append new node with value: Second Node                       # Confirms |"Second Node"| was appended correctly
>>> dllist.head.value                                         # If appended correctly then |dllist.head.value| should remain and result in the |"First Node"|
'First Node'                                                  # Confirms |"First Node| was appended correctly
>>> dllist.tail.value                                         # Checks for the tail node again
'Second Node'                                                 # Confirms |"Second Node"| is not the tail node
>>> dllist.head.next.value                                    # Checks for the next head value
'Second Node'                                                 # Confirms the next head value is the |"Second Node"| and proves head node has a link to the second node
>>> dllist.tail.prev.value                                    # Checks for the previous tail valie
'First Node'                                                  # Confirms the previous tail value is the |"First Node"| and proves the |"Second Node"| has a link to the head node
>>> dllist.head.prev.value                                    # Head node is the first node + tail node is the second node so the heads node should contain a previous value of |None| since the first node cannot have a previous node
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'value'    # Confirms there is indeed no existing value before the head value as it cannot have a previous value. You cannot access values that do not logically exist.
>>> dllist.tail.next.value                                    # Checks for the next tail value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'value'    # Confirms there is no existing value after the tail value. You cannot access values that do not logically exist.
>>> dllist.append("Third Node")                               # Appending a |"Third Node"| by using dllist.append("")
Append new node with value: Third Node                        # Confirms |"Third Node"| was appended correctly
>>> dllist.tail.value                                         # Checks for the tail value
'Third Node'                                                  # Confirms the tail value is now |"Third Node"| after appending
>>> dllist.tail.prev.value                                    # Checks previous tail value
'Second Node'                                                 # Results in |"Second Node"| and confirms there is a link between the |"Third Node"| and the |"Second Node"|
>>> dllist.tail.prev.prev.value                               # Checks the previous, previous tail value
'First Node'                                                  # Results in |"First Node"| and confirms there is a link between |Third...Second, and First Node|
>>> dllist.head.next.next.value                               # Checks the next next head value
'Third Node'                                                  # Results in |"Third Node"|

"""