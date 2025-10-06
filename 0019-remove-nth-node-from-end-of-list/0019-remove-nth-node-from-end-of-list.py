# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            head = None
            return
        x = 0
        current = head
        while current:
            current = current.next
            x += 1

        if x == n:
            head = head.next
            return head
        
        pos = x - n

        current = head

        i = 0
        while current and i < pos - 1:
            current = current.next
            i += 1

        if not current:
            return
        
        if current.next.next:
            current.next = current.next.next
            return head
        
        current.next = None
        return head