class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(n):
            if n in cache:
                return cache[n]
            
            val = 0
            if n >= 0:
                val = nums[n] + max(dfs(n - 2), dfs(n - 3))
            
            cache[n] = val
            return val
        
        n = len(nums) - 1
        return max(dfs(n), dfs(n - 1))