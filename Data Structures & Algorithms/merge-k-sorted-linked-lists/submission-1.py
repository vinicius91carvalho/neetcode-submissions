# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def merge_lists(self, list_node1: ListNode, list_node2) -> ListNode:
        if not list_node1:
            return list_node2
        elif not list_node2:
            return list_node1
        
        list_node_head = None
        if list_node1.val <= list_node2.val:
            list_node_head = ListNode(list_node1.val)
            list_node1 = list_node1.next
        else:
            list_node_head = ListNode(list_node2.val)
            list_node2 = list_node2.next
        tail = list_node_head

        while list_node1 and list_node2:
            if list_node1.val <= list_node2.val:
                tail.next = ListNode(list_node1.val)
                list_node1 = list_node1.next
            else:
                tail.next = ListNode(list_node2.val)
                list_node2 = list_node2.next
            tail = tail.next
        
        if list_node1:
            tail.next = list_node1
        elif list_node2:
            tail.next = list_node2
        
        return list_node_head
            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists_length = len(lists)

        if lists_length > 1:
            list_node = lists[0]
            for i in range(1, lists_length):
                list_node = self.merge_lists(list_node, lists[i])

            return list_node
        elif lists_length == 1:
            return lists[0]
        else:
            return None
            
        