# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head

        while current:
            length += 1
            current = current.next
        
        if length == 1:
            head = None
            return head
        
        current = head
        prev = None
        for i in range(length - n):
            prev = current
            current = current.next
        if prev:
            prev.next = current.next
        else:
            head = current.next
            current.next = None
        return head
        