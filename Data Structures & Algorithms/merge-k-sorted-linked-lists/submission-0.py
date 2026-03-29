# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def _is_remaining(lists):
            for l in lists:
                if l:
                    return True
            return False
        
        head = ListNode()
        it = head
        while _is_remaining(lists):
            min_node = ListNode(val = float('inf'))
            min_idx = 0
            for idx, l in enumerate(lists):
                if l and l.val < min_node.val:
                    min_node = l
                    min_idx = idx
            it.next = lists[min_idx]
            it = it.next
            lists[min_idx] = lists[min_idx].next
                
        
        return head.next
            