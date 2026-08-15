# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root: return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # q, level = deque([root]) if root else None, 0
        # while q:
        #     level += 1
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left: q.append(node.left)
        #         if node.right: q.append(node.right)
        # return level

        stack, m_depth = [[root, 1]] if root else None, 0
        while stack:
            node, depth = stack.pop()
            m_depth = max(m_depth, depth)

            if node.right:
                stack.append([node.right, depth + 1])
            if node.left:
                stack.append([node.left, depth + 1])
        return m_depth




