# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = set()
        current = head
        prev = None
        while current:
            if current.val not in x:
                x.add(current.val)
            else:
                if current.next:
                    prev.next = current.next
                    current = prev
                else:
                    prev.next = None
            prev = current
            current = current.next
        return head