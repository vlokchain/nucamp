# DEFINE: Queue abstract data type as a Python class, with the help of a Linked List.

# RECALL: A linked list needs a node that can hold a value and a reference to the next node

class Node:                            # Node for singly linked list
    def __init__(self, value):         
        self.value = value         
        self.next = None               # Only has next attribute
 
class Queue:                           # Queue class with |init| constructor method
    def __init__(self):
        self.head = None               # Attribute |self.head| to keep track of the oldest first in item
        self.tail = None               # Attribute |self.tail| to keep track of the newest last in item
        self.num_nodes = 0             # Keeps counter of the nodes in our queue: we begin with 0

    def size(self):                    # This method will check the size of the Queue
        return self.num_nodes          # Returns the future object |num_nodes| attribute

    def enqueue(self, value):          # Implement enqueue. Meaning we will be adding a node to the tail end of our queue
        new_node = Node(value)         # Start by creating this node from the node class with a passed in value

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:          # Check to see if Queue is empty by checking if |self.head| is None
            # self.head = new_node     # In this case we will set the new node as the value for |self.head|
            # self.tail = new_node     # In this case we will set the new node as the value for |self.tail|
            self.head = self.tail = new_node  # Same as above two lines: new node is the value for |self.head| and |self.tail| (this is called a multiple assignment)
        else:                          # Else: meaning if its not empty
            self.tail.next = new_node  # If not empty we will set the current Queue's |self.tail.next| attribute to the new node
            self.tail = new_node       # Then we'll replace the |self.tail| attribute with a reference to the |new_node|: this means previous tail is now linked to new node and the new node is the tail.
# Remove indentation and away from |else| statement so the statement can occur wether or the queue was empty (line 23)
        self.num_nodes += 1            # We will increment |self.num_nodes| by 1

    def dequeue(self):                 # dequeue() method
        if self.head is None:
            return None

        dequeue_node_value = self.head.value
        self.head = self.head.next     # Sets the next node in the queue to be the new head. This removes the previous head from the queue
        self.num_nodes -= 1            # Decrements the counter by 1
        return dequeue_node_value      # Saves the value of the dequeue node and uses it as a return value from this method

q = Queue()                            # Instantiating |Queue| object from the class
q.enqueue('a')                         # Using enqueue() method to add string value of "a"
q.enqueue('b')                         # Using enqueue() method to add string value of "b"
q.enqueue('c')                         # Using enqueue() method to add string value of "c"

print("Pass" if (q.size() == 3) else "Fail")       # Testing size() method works correctly by printing Pass if size = 3 and Fail if not. Prints: Pass
q.enqueue(4)                                       # Enqueue one more node. This brings the count of nodes to 4.
print("Pass" if (q.size() == 4) else "Fail")       # Checking size() method again by printing printing Pass if size = 4 and Fail if not. Prints: Pass

# Now we test dequeuing: right now the head for the head node for the queue object has a value of "a"
print("Pass" if (q.dequeue() == 'a') else "Fail")  # If we call the dequeue method for the queue object it should remove the head node and return the value of "a". Queue now has a size of 3 instead of 4. Prints: Pass
print("Pass" if (q.dequeue() == 'd') else "Fail")  # If we call it again it will return "b" because that is the new head once "a" has been dequeued. Prints: Fail. But this doesn't stop dequeue() method from being called. It only fails the comparison of the dequeue() method return value to the string "d". The cue size will strill decrement by 1. Meaning it now ahs a size of 2 instead of 3.
print("Pass" if (q.size() == 2) else "Fail")       # We can test the size is now = 2. Prints: Pass
