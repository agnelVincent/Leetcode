# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        n = 0
        def dfs(node):
            nonlocal n 
            if node:
                n += 1
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return n
        