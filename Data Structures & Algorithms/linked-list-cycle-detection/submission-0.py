# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowCurrent = head
        slowSignal = 0
        if not head:
            return False
        fastCurrent = head.next
        while fastCurrent:
            if slowSignal:
                slowCurrent = slowCurrent.next
                slowSignal = 0
            else:
                slowSignal = 1

            if fastCurrent == slowCurrent:
                return True
            fastCurrent = fastCurrent.next
            
        return False
