# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        res_head = None
        left = 0
        currentl1 = l1
        currentl2 = l2

        while True:
            if not currentl1 and not currentl2 and not left:
                break
                
            val = 0
            val += left
            if currentl1:
                val += currentl1.val
                currentl1 = currentl1.next
            if currentl2:
                val += currentl2.val
                currentl2 = currentl2.next
            
            if val > 9:
                v = str(val)
                if not res_head:
                    res_head = ListNode(int(v[-1]))
                    current = res_head
                    left = int(v[:-1])
                    continue
                else:
                    current.next = ListNode(int(v[-1]))
                left = int(v[:-1])

            else:
                if not res_head:
                    res_head = ListNode(val)
                    current = res_head
                    continue
                else:
                    current.next = ListNode(val)
                left = 0

            current = current.next

        return res_head