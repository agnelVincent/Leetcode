# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_dist = float('inf')
        prev = None
        def dfs(node):
            nonlocal min_dist , prev
            if node:
                dfs(node.left)
                if prev:
                    if abs(prev.val - node.val) < min_dist:
                        min_dist = abs(prev.val - node.val)
                prev = node
                dfs(node.right)
        dfs(root)
        return min_dist

        