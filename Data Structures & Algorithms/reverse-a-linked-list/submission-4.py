# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0 -> 1 -> 2 -> 3
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # early exit
        if not head:
            return head
       
        # save end of list
        curr = head
        while curr.next:
            curr = curr.next
        new_head = curr

        # recucrsively reverse the list
        def reverse(node):
            if node.next:
                prev = reverse(node.next)
                prev.next = node
            return node
        
        reverse(head)
        head.next = None

        return new_head