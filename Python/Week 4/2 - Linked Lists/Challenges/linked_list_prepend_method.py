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

        node = self.head                     # |node| variable = |self.head| head node
        while node.next is not None:         # |while| loop to traverse the linked list until we reach tail node: loop condition will exit the loop when it reaches a node whose next attribute is |None|
            node = node.next                 # This means every time we enter the loop body we traverse from one node to the next

        node.next = new_node                 # When we reach the tail node and exit the loop. The variable |node| contains a reference to the tail node. This instantiates the node we created into the new tail node.
        print("Appended new Node with value:", node.next.value)

    def prepend(self, value):                # Adding method called |prepend()| with parameters (|self|, |value|)
        new_node = Node(value)               # Instantiate a new object of the Node class passing the parameter of the |prepend()| method
        if self.head is None:                # If the self object does not have a head attribute
            self.head = new_node             # Assign the new Node object you just instantiated as the head
            print("Head Node Created:", self.head.value) # print the message "Head Node created: " followed by the value of the node.
        node = self.head
        while node.next is not None:        # For the case in which the self object already has a head Node
            node = node.next            # You will then write code to assign the new Node object as the new head.
        node.next = new_node            # The existing head must then be linked to the new head. 
        print("Prepended new Head Node with value:", node.next.value)
        print("Node following head is:", self.head.value)



llist = LinkedList()                         # Creating a new linked list object named |llist| by isntantiating from the |LinkedList| class.
llist.prepend("First Node")
llist.prepend("Inserted New First Node")
