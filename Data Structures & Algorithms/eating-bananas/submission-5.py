class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(k):
            curr_h = 0
            for bananas in piles:
                curr_h += math.ceil(bananas/k)
            return curr_h <= h
        
        left, right = 1, max(piles)
        result = right
        while left <= right:
            k = left + (right - left) // 2
            if can_eat(k):
                right = k - 1
                result = k
            else:
                left = k + 1
        
        return result
        
        