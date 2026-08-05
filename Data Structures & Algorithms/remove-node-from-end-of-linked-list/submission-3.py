# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        first = sec = dummy
        for i in range(n+1):
            sec = sec.next
        
        while sec:
            first = first.next
            sec = sec.next
        
        first.next = first.next.next

        return dummy.next