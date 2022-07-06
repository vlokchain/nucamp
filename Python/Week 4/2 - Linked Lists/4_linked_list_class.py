# HOW TO HANDLE A CALLED METHOD WHILE THE LINKED LIST DOES NOT HAVE A HEAD NODE/EMPTY LIST:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:               # Instantiating a |LinkedList| with
    def __init__(self):         # A linked lsit must always know where its head is
        self.head = None        # |self.head| = |None| initializes any future objects head attribute to |None|

    def append(self, value):    # Setting up an append method for the |LinkedList| class 
        new_node = Node(value)  # Instantiate a |new node| using the |Node| class as the (value) argument. This |new_node| will have the next attribute of none due to |Node| class constructor.
  
        if self.head is None:                             # To append to our |LinkedList| object we find tail node of list to link to the head node
            self.head = new_node                          # Set the |new_node| we made as the head node
            print("Head Node Created:", self.head.value)  # Tests the value of |self.head| changed correctly
            return                                        # Use |return| to return out of this method.

# HOW TO HANDLE NON-EMPTY LIST WITH A HEAD & IMPLEMENT AN APPEND METHOD:

        node = self.head                     # |node| variable = |self.head| head node
        while node.next is not None:         # |while| loop to traverse the linked list until we reach tail node: loop condition will exit the loop when it reaches a node whose next attribute is |None|
            node = node.next                 # This means every time we enter the loop body we traverse from one node to the next

        node.next = new_node                 # When we reach the tail node and exit the loop. The variable |node| contains a reference to the tail node. This instantiates the node we created into the new tail node.
        print("Appended new Node with value:", node.next.value)

llist = LinkedList()                         # Creating a new linked list object named |SecondList| by isntantiating from the |LinkedList| class.
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node") 