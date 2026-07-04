class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        current = self.head
        while current and i <= index:
            if i == index:
                return current.val
            current = current.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return

        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            return self.addAtHead(val)

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)

        current = self.head
        i = 0
        while current and i < index - 1:
            current = current.next
            i += 1

        if not current:
            return False

        new_node = Node(val)
        if current.next:
            new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return False

        if index == 0:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return

        current = self.head
        i = 0
        while current and i < index - 1:
            current = current.next
            i += 1
        
        if not current:
            return False
        
        if current.next and current.next.next:
            current.next = current.next.next
            return 
        
        if current.next and not current.next.next:
            current.next = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)