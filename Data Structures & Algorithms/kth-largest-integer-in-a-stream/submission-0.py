class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums.copy()
        self.k = k
        heapq.heapify_max(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        holder = []
        for i in range(self.k):
            holder.append(heapq.heappop_max(self.heap))
        result = holder[-1]
        for n in holder:
            heapq.heappush_max(self.heap, n)
        return result
        
