# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list1, list2 = head, slow.next
        slow.next = None

        prev, curr = None, list2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        list2 = prev

        while list1 and list2:
            nxt1, nxt2 = list1.next, list2.next
            list1.next = list2
            list1 = nxt1
            list2.next = list1
            list2 = nxt2
