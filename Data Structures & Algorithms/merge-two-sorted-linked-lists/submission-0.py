# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def insert_ordered(self, list3_head: ListNode, node: ListNode) -> ListNode:
        if list3_head == None:
            return ListNode(node.val)
        elif node.val <= list3_head.val:
            return ListNode(node.val, list3_head)
        else:
            curr = list3_head
            prev = None
            while curr != None:
                if node.val <= curr.val:
                    prev.next = ListNode(node.val, curr)
                    return list3_head
                prev = curr  
                curr = curr.next
            prev.next = ListNode(node.val)
            return list3_head    
        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3_head = None

        curr = list1
        while curr != None:
            list3_head = self.insert_ordered(list3_head, curr)
            curr = curr.next
        
        curr = list2
        while curr != None:
            list3_head = self.insert_ordered(list3_head, curr)
            curr = curr.next

        return list3_head