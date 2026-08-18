# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.k = k
        
        # def dfs(root):
        #     if not root: return

        #     left = dfs(root.left)
        #     if left: return left

        #     self.k -= 1
        #     if self.k == 0: return root.val
            
        #     right = dfs(root.right)
        #     if right: return right
        
        # return dfs(root)

        count, stack, cur = 0, [], root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            count += 1
            if count == k: return cur.val

            cur = cur.right

            






