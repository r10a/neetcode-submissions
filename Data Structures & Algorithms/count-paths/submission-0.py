class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = dict()

        def dfs(x, y):
            if x >= m or y >= n:
                return 0
            
            if (x, y) in cache:
                return cache[(x, y)]
            
            if x == (m-1) and y == (n-1):
                return 1
            
            val = dfs(x + 1, y) + dfs(x, y + 1)
            cache[(x, y)] = val
            return val
        
        return dfs(0, 0)
