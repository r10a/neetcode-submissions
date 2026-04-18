class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for n in counts.items():
            heapq.heappush(heap, (n[1], n[0]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n[1] for n in heap]