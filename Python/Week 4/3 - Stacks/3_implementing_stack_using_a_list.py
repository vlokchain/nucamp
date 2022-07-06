class Stack:                        # Implementing |Stack| class
    def __init__(self):
        self.items = []             # Attribute called |self.items| initialized to empty Python List

    def push(self, value):          # Implement push() method
        self.items.append(value)    # Use python list method of |append()| for the Stack's push method (append adds to the end)

    def pop(self):                  # Implement pop() method (pop removes from the end) so end of list will be the head of the stack
        if self.size() == 0:        # Returns |None| if length of list is == 0
            return None
        return self.items.pop()     # If list is not empty we'll use list method pop() to remove the top node. That value will then be used as the Stack methods pop() return value

    def size(self):                 # To refer to the length or size of the stack easily
        return len(self.items)

stack = Stack()                    # Instantiate Stack object from the class
stack.push(1)                      # push() 1 items
stack.push(2)                      # push() 2 items
stack.push(3)                      # push() 3 items
stack.push(4)                      # push() 4 items

print("Pass" if (stack.size() == 5) else "Fail")  # This will print Fail: Print pass if stack size == 5 or Print Fail if not
stack.push(5)                                     # push() 5 items
print("Pass" if (stack.size() == 5) else "Fail")  # This will print Pass: Print pass if stack size == 5 or Print Fail if not

print("Pass" if (stack.pop() == 5) else "Fail")   # This will print Pass : Print pass if return value == 5 from popping top item off Stack or Print Fail if not
print("Pass" if (stack.pop() == 4) else "Fail")   # This will print Pass : Print pass if return value == 5 from popping top item off Stack or Print Fail if not