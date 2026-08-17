# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(root, max_sofar):
            if not root: return
                      
            if (max_sofar and root.val >= max_sofar[-1]) or not max_sofar:
                self.count += 1
                max_sofar.append(root.val)
            else:
                max_sofar.append(max_sofar[-1])

            dfs(root.left, max_sofar)
            dfs(root.right, max_sofar)
            max_sofar.pop()
        dfs(root, [])
        return self.count