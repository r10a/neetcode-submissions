# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = []

        for l in lists:
            if l:
                heapq.heappush(min_heap, NodeWrapper(l))
        
        head = ListNode()
        it = head
        while min_heap:
            min_node_wrapper = heapq.heappop(min_heap)
            it.next = min_node_wrapper.node
            it = it.next
            if min_node_wrapper.node.next:
                heapq.heappush(min_heap, NodeWrapper(min_node_wrapper.node.next))
        
        return head.next