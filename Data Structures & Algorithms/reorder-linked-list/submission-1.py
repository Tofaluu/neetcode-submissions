# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        if length == 1:
            return None
        
        current2 = head
        prev = None
        for i in range((length + 1) // 2):
            prev = current2
            current2 = current2.next

        prev.next = None

        prev2 = None
        while current2:
            next = current2.next
            current2.next = prev2
            prev2 = current2
            current2 = next

        head2 = prev2
        dummy = ListNode()
        tail = dummy

        while head:
            tail.next = head
            head = head.next
            tail = tail.next
            if head2:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
        
        return None

        



        
