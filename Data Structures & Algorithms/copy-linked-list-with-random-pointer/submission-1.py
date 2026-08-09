"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        prev, curr, dummy = None, head, Node(0)
        new_curr = dummy

        while curr:
            # create new node and move to it
            new_curr.next = Node(curr.val, None, None)
            new_curr = new_curr.next

            # add the mapping
            old_to_new[curr] = new_curr

            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        return dummy.next