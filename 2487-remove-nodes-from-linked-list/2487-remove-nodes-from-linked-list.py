# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        
        max_val = float('-inf')
        last_visited = None
        while stack:
            node = stack.pop()
            if node.val >= max_val:
                max_val = node.val
                node.next = last_visited
                last_visited = node
        return last_visited
            