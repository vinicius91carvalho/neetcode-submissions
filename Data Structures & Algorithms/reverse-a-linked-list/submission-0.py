# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        next = None
        while curr != None:
            temp = curr.next
            # curr = head, curr.next = next1
            # temp = next1, temp.next = next2
            # next = None
            curr.next = next
            # curr = head, curr.next = None
            # temp = next1, temp.next = next2
            # next = None
            next = curr
            # curr = head, curr.next = None
            # temp = next1, temp.next = next2
            # next = head, curr.next = None
            curr = temp
            # curr = next1, curr.next = next2
            # next = head, curr.next = None
        return next

            

            