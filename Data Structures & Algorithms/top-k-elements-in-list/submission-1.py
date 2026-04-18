class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = defaultdict(int)
        for n in nums:
            lookup[n] += 1
        result = sorted(lookup.items(), key=lambda x: x[1], reverse=True)[:k]
        return [k[0] for k in result]
