class ListNode:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class Queue:
    def __init__(self, nodes: List) -> None:
        self.head = ListNode(nodes[0])
        self.tail = None
        self.count = len(nodes)
        self.count_circular = 0
        self.count_squares = 0

        node = self.head
        for i in range(1, len(nodes)):
            node.next = ListNode(nodes[i])
            node = node.next
        
        self.tail = node

        self.count_circular_and_squares(nodes)
    
    def count_circular_and_squares(self, nodes: List) -> None:
        for i in range(len(nodes)):
            if nodes[i] == 0:
                self.count_circular += 1
            else:
                self.count_squares += 1 
    
    def move_head_to_tail(self) -> None:
        node = self.head.next
        self.tail.next = ListNode(self.head.value)
        self.tail = self.tail.next
        self.head = node

    
    def remove_head(self) -> ListNode:
        if self.head.value == 0:
            self.count_circular -= 1
        else:
            self.count_squares -= 1

        node = self.head
        self.head = self.head.next
        self.count -= 1
        return node

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = Queue(students)
        while sandwiches:
            if sandwiches[0] == 0 and students_queue.count_circular <= 0 or sandwiches[0] == 1 and students_queue.count_squares <= 0: 
                break

            if students_queue.head.value == sandwiches[0]:
                students_queue.remove_head()
                sandwiches = sandwiches[1:]
            else:
                students_queue.move_head_to_tail()
        return students_queue.count
    