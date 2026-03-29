class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid) - 1
        if grid[0][0] != 0 or grid[N][N] != 0:
            return -1
        
        queue1 = deque()
        queue1.append((0, 0))
        queue2 = deque()
        queue2.append((N, N))

        grid[0][0] = -1
        grid[N][N] = -2

        start, end = -1, -2
        path = 2
        while queue1 and queue2:
            for _ in range(len(queue1)):
                x, y = queue1.popleft()
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= N and 0 <= ny <= N and not (dx == dy == 0):
                            if grid[nx][ny] == 0:
                                grid[nx][ny] = start
                                queue1.append((nx, ny))
                            elif grid[nx][ny] == end:
                                return path
            queue1, queue2 = queue2, queue1
            start, end = end, start
            path += 1
        
        return -1