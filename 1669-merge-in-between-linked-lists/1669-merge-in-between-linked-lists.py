# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current = list1
        prev = None
        i = 0
        while i < a:
            prev = current
            current = current.next
            i += 1

        while a <= b:
            current = current.next
            a += 1

        prev.next = list2
        while prev.next:
            prev = prev.next

        prev.next = current

        return list1
          

        
    