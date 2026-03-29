class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        result = float('inf')

        def _is_possible_to_eat(k):
            curr_piles = piles[:]
            hour_counter = 0
            for i in curr_piles:
                hour_counter += math.ceil(i / k)
            return hour_counter <= h

        while left <= right:
            m = left + (right - left) // 2

            is_possible_to_eat = _is_possible_to_eat(m)
            print(left, m, right, is_possible_to_eat)

            if is_possible_to_eat:
                result = min(result, m)
                right = m - 1
            else:
                left = m + 1
        
        return result
