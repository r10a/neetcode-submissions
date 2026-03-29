# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0,1,2
# 0 -> 1 -> 2 -> None
# it#1: new_head = head = 0
#       new_head = 2 -> 1 -> None
#       2 -> 1 -> 0 -> 1 -> 2 -> None
#       2 -> 1 -> 0 -> None
# it#2: new_head = head = 1
#       new_head = 2 -> None
#       2 -> 1 -> 2 -> None
#       2 -> 1 -> None
# it#3: new_head = head = 2
#       2 -> None




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head:
            return head
        
        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head
