# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0,1,2,3
# 0 -> 1 -> 2 -> 3 -> None
# head = 0
# curr = 1
# 0 -> None
# while it#1
#   next = 2
#   1 -> 0 -> None
#   head = 1
#   curr = 2
# while it#2
#   next = 3
#   2 -> 1 -> 0 -> None
#   head = 2
#   curr = 3
# while it#3
#   next = None
#   3 -> 2 -> 1 -> 0 -> None
#   head = 3
#   curr = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case
        if not head:
            return head
        
        # kick things off
        curr = head.next
        head.next = None

        while curr:
            next = curr.next
            curr.next = head
            head = curr
            curr = next
        
        return head

