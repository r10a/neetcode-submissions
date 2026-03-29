import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(point[0]**2 + point[1]**2, point[0], point[1]) for point in points]
        heap = []
        for point in distance:
            heapq.heappush_max(heap, point)
            if len(heap) > k:
               heapq.heappop_max(heap)
        return [[point[1], point[2]] for point in heap]
        