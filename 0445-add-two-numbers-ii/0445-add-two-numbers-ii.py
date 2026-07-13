# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 , n2 = [], []
        currentl1 , currentl2 = l1, l2
        while currentl1 and currentl2:
            n1.append(currentl1.val)
            n2.append(currentl2.val)
            currentl1 = currentl1.next
            currentl2 = currentl2.next

        if currentl1:
            while currentl1:
                n1.append(currentl1.val)
                currentl1 = currentl1.next
        
        if currentl2:
            while currentl2:
                n2.append(currentl2.val)
                currentl2 = currentl2.next

        res = []
        left = 0
        r = 0
        while True:
            if not left and not n1 and not n2:
                break
            r = left
            if n1:
                r += n1.pop()
            if n2:
                r += n2.pop()
            left = r // 10
            res.append(r % 10)

        res_head = ListNode(0)
        current = res_head
        for i in res[::-1]:
            current.next = ListNode(i)
            current = current.next
        
        return res_head.next


