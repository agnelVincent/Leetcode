# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        x = {}
        def dfs(node):
            if node:
                if node.val not in x:
                    x[node.val] = 0
                x[node.val] += 1
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        res = max(x.values())
        return [i for i in x if x[i] == res]