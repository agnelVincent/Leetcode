# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head and head.val == val:
            return self.removeElements(head.next , val)

        current = head
        prev = None

        while current:
            print(current.val)
            if current.val == val:
                if current.next:
                    prev.next = current.next
                    current = prev.next
                    continue
                else:
                    prev.next = None
            prev = current
            current = current.next
        return head

        