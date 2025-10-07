# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node , path):
            print(path)
            if node.left:
                dfs(node.left , path + str(node.left.val))
            if not node.left and not node.right:
                res.append(path)
            if node.right:
                dfs(node.right , path + str(node.right.val))
        dfs(root , str(root.val))
        print(res)
        return sum([int(i) for i in res])
        