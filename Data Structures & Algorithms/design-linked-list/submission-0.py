class Node():
    def __init__(self, val: int, prev: Optional[Node] = None, next: Optional[Node] = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __get_node(self, index: int) -> Optional[Node]:
        if self.head and index >= 0 and index < self.length:
            curr = self.head
            while curr != None and index > 0:
                curr = curr.next
                index -= 1
            return curr
        return None

    def get(self, index: int) -> int:
        node = self.__get_node(index)
        if node:
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, None, self.head)
        if self.head:
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val, self.tail)
        if self.tail:
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.tail = node
            self.head = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            return self.addAtTail(val)
        elif index == 0:
            return self.addAtHead(val)
        elif index > self.length:
            return
        
        curr = self.__get_node(index)
        prev = curr.prev
        new_node = Node(val, prev, curr)
        prev.next = new_node
        curr.prev = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if self.length == 1 and index == 0:
            self.head = None
            self.tail = None
            self.length = 0
            return
        
        curr = self.__get_node(index)
        if curr:
            if curr == self.head:
                self.head = self.head.next
                self.head.prev = None
            elif curr == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                prev, next = curr.prev, curr.next
                prev.next = next
                next.prev = prev
            self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)