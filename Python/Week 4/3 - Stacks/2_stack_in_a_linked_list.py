class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None              # Attribute #1 to keep track of the |Stack| class head
        self.num_nodes = 0            # Attribute #2 to keeo trac of the number of nodes in the |Stack| class at all times (not neccessary to fulfill definitian of a Stack data type)

    def push(self, value):            # The |push()| method is central to the definiton of a Stack
        new_node = Node(value)        # Instantiate new node from the node class which will hold the |value| parameter

# We want to push this node to the end of our Stack. We will use the |head| end (not the tail end) to represent the Stack's top
# To push the node to the top of a Stack implemented with a linked list we must make it the new head. To do this:

        if self.head is not None:     # We first check if the head is not None
            new_node.next = self.head # New node is linked to the current head node

        self.head = new_node          # Make stack treat the new node as the new head node
        self.num_nodes += 1           # Increment Stack's counter for the number of nodes by one

    def pop(self):                    # Create pop() method to remove the current head of the stack w/ no parameters except from |self|
        if self.head == None:         # Checks if there are not items in the stack
            return None               # In this case we will |return None|
            
        pop_node = self.head.value    # Save the value of the current head to a temporary variable called |pop_node|
        self.head = self.head.next    # Change the self/head to reference the next node in the linked list
        self.num_nodes =- 1           # Since we are removing a node we need to decrement the |num_nodes| attribute by 1
        return pop_node               # Finally we use pop_node as our return value. This lets the caller know this is the value popped off the stack

# Instantiate an object from the Stack class and push items to it

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# Print statement will print pass if our Stack's object number of nodes is equal to 5 else it will print Fail.
print("Pass" if (stack.num_nodes == 5) else "Fail") # It will Fail at this point as we have only pushed 4 nodes or stack.num_nodes == 4
stack.push(5)                                       # Adding another node to Stack
print("Pass" if (stack.num_nodes == 5) else "Fail") # It will Pass as we now have 5 nodes or stack.num_nodes == 5

print("Pass" if (stack.pop() == 5) else "Fail")     # It will Pass 
print("Pass" if (stack.pop() == 4) else "Fail")     # It will also Pass