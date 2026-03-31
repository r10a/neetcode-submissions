class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        # no path
        if obstacleGrid[0][0] == 1 or obstacleGrid[M - 1][N - 1] == 1:
            return 0

        obstacleGrid[M - 1][N - 1] = 1

        for y in range(M - 1, -1, -1):
            for x in range(N - 1, -1, -1):
                # skip destination cell
                if y == M - 1 and x == N - 1:
                    continue
                
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = 0
                else:
                    down = obstacleGrid[y + 1][x] if y + 1 < M else 0
                    right = obstacleGrid[y][x + 1] if x + 1 < N else 0
                    obstacleGrid[y][x] = down + right
        
        return obstacleGrid[0][0]