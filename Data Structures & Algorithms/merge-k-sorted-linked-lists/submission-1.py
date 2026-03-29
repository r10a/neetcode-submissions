# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def _divide(arr, s, e):
            if e - s < 0:
                return None
            if e - s == 0:
                return arr[s]
            
            m = s + (e - s) // 2

            left = _divide(arr, s, m)
            right = _divide(arr, m + 1, e)

            return _conquer(arr, left, right)
        
        def _conquer(arr, left, right):
            head = ListNode()
            it = head
            while left and right:
                if left.val < right.val:
                    it.next = left
                    left = left.next
                else:
                    it.next = right
                    right = right.next
                it = it.next
            
            if left:
                it.next = left
            
            if right:
                it.next = right
            
            return head.next
        
        return _divide(lists, 0, len(lists) - 1)
                