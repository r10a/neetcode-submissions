# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def _merge(left, right):
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
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(_merge(left, right))
            lists = merged_lists

        return lists[0]
