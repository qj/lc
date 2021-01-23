class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        to_print = ""
        while self:
            to_print += str(self.val)
            self = self.next
        return to_print

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head 

    while curr:
        curr_next = curr.next
        curr.next = prev
        prev = curr 
        curr = curr_next 
    
    return prev

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(reverseList(head))
    