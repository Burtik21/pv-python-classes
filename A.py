class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingSinglyLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Cannot pop from an empty stack.")
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def count(self):
        return self.size

    def clear(self):
        self.top = None
        self.size = 0

    def popAll(self):
        elements = []
        while self.top is not None:
            elements.append(self.pop())
        return elements

    # Overload the __contains__ method for 'in' operator functionality
    def __contains__(self, item):
        current = self.top
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    # Overload the __reversed__ method to reverse the stack
    def __reversed__(self):
        reversed_stack = StackUsingSinglyLinkedList()
        current = self.top
        while current is not None:
            reversed_stack.add(current.data)
            current = current.next
        return reversed_stack

    # A helper method to view the stack contents as a list (for testing purposes)
    def to_list(self):
        elements = []
        current = self.top
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements


# Example usage
stack = StackUsingSinglyLinkedList()

stack.add(10)
stack.add(20)
stack.add(30)
stack.add(40)
stack.add(50)

print(f"Popped item: {stack.pop()}")
print(f"Stack size: {stack.count()}")

print(f"Stack contents (before popAll): {stack.to_list()}")
print(f"Popped all: {stack.popAll()}")
print(f"Stack size after popAll: {stack.count()}")

stack.add(100)
stack.add(200)
stack.add(300)

# Check if an element is in the stack using the 'in' operator
if 200 in stack:
    print("200 is in the stack")

if 400 not in stack:
    print("400 is not in the stack")

# Reverse the stack
reversed_stack = reversed(stack)
print(f"Original stack (after reversing): {stack.to_list()}")
print(f"Reversed stack contents: {reversed_stack.to_list()}")
