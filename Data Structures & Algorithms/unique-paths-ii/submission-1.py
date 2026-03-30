class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid) - 1
        N = len(obstacleGrid[0]) - 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[M][N] == 1:
            return 0

        cache = {}

        def dfs(x, y):
            if x > M or y > N or obstacleGrid[x][y] == 1:
                return 0
            
            cache_index = (x, y)
            if cache_index in cache:
                return cache[cache_index]

            if x == M and y == N:
                return 1
            
            val = dfs(x + 1, y) + dfs(x, y + 1)
            cache[cache_index] = val
            return val
        
        return dfs(0, 0)