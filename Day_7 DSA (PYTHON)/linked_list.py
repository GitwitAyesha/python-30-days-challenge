class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next: 
            itr = itr.next
        
        itr.next = Node(data, None)  
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return 

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                return 
            itr = itr.next
            count += 1
        raise Exception("Index out of range")
    def remoove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return 
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
        


    def print_list(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = '-->' if itr.next else ''
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

if __name__ == '__main__':
    root = LinkedList()
    root.insert_at_end(20)
    root.insert_at_beginning(5)
    root.insert_at(1, 25)  
    root.insert_at_beginning(10)
    root.insert_at_beginning(15)
    root.remoove_at(1)
    
    root.print_list()  
    print("Length:", root.get_length())  