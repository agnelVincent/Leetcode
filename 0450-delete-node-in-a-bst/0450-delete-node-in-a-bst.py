# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete_node(node , key):
            if not node:
                return None
            if key < node.val:
                node.left = delete_node(node.left , key)
            elif key > node.val:
                node.right = delete_node(node.right , key)
            else:
                if not node.left and not node.right:
                    return None
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                res = find_min(node.right)
                node.val = res.val
                node.right = delete_node(node.right , res.val)
            return node

        def find_min(node):
            while node.left:
                node = node.left
            return node
        
        return delete_node(root , key)