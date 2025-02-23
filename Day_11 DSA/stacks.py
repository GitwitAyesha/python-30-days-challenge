class stacks:
    def __init__(self):
        self.container = []
    def push(self,val):
        self.container.append(val)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.container.pop()
    # top position
    def peek(self):
        if self.is_empty():
            raise ImportError("peek from empty stack")
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
stack = stacks()
stack.push(3)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.size())
print(stack.peek())
print(stack.is_empty())



# s = []
# s.append(2)
# s.append(3)
# s.append(4)
# s.append(5)
# print(s)
# s.pop()
# print(s)

