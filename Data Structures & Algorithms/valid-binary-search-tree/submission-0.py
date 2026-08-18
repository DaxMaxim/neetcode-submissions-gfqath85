# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, lower, upper):
            if not root: return True
            return (lower < root.val < upper) and dfs(root.left, lower, min(upper, root.val)) and dfs(root.right, max(lower, root.val), upper)

        return dfs(root, float("-inf"), float("inf"))