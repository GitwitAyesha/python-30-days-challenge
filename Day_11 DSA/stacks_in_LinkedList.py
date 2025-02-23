# class representing node in Linked List
class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None
class Stacks:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            print("\n Stack underflow")
            return None
        else:
            temp = self.head
            popped_data = temp.data
            self.head = self.head.next
            del temp
            return popped_data
    def peek(self):
        if self.is_empty():
            print("Stack is empty : Cannot peek.")
            return None
        else:
            # print("\ Stack is empty")
            return self.head.data

st = Stacks()
st.push(1)
st.push(2)
st.push(3)
print(st.is_empty())
print(st.pop())
print(st.peek())
