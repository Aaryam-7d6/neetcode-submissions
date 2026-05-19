# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        current = head
        while current:
            next = current.next
            current.next = temp.next
            temp.next = current
            current = next
        return temp.next
        