# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = 1
        current = head
        while current:
            x += 1
            current = current.next
        mid = 0
        if x%2 == 1:
            mid = x // 2 + 1
        else:
            mid = x // 2
        
        temp = None
        x = 1
        current = head
        while current and x < mid - 1:
            current = current.next
            x += 1

        if current.next:
            current.next = current.next.next
        else:
            return None
        return head