class Solution:
    def rob(self, nums: List[int]) -> int:
        d1, d2 = 0, 0
        for n in nums:
            temp = max(n + d1, d2)
            d1 = d2
            d2 = temp
        return d2