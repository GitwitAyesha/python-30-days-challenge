class Node:
    def reverseList(self,head : Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        nxt = current.next
        while current != None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head = prev
        return head
            
