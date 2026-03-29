class Solution:
    def climbStairs(self, n: int) -> int:
        
        lookup = defaultdict(int)
        def dfs(n):
            if n in lookup:
                return lookup[n]
            
            if n > 1:
                val = dfs(n - 2) + dfs(n - 1)
            elif n == 1 or n == 0:
                val = 1
            else:
                val = 0
            lookup[n] = val
            return val
        
        return dfs(n)