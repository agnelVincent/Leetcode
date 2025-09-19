# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:
            prev = current
            current = current.next
            i = min(current.val , prev.val)
            while i > 0:
                if current.val % i == 0 and prev.val % i == 0:
                    new_node = ListNode(i)
                    new_node.next = prev.next
                    prev.next = new_node
                    break
                i -= 1
        return head