class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones.copy()
        heapq.heapify_max(heap)

        while len(heap) > 0:
            x = heapq.heappop_max(heap)
            if len(heap) == 0:
                return x
            y = heapq.heappop_max(heap)
            if x != y:
                heapq.heappush_max(heap, abs(y - x))

        return 0
