# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        def preorder(node):
            if node:
                stack.append(node)
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        i = 1
        while i < len(stack):
            stack[i-1].right = stack[i]
            stack[i - 1].left = None
            i += 1

        