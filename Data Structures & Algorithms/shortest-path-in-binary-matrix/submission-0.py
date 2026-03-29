class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.append((1, 0, 0))
        target_x, target_y = len(grid) - 1, len(grid[0]) - 1
        results = []

        while queue:
            c_path_length, x, y = queue.popleft()
            if grid[x][y] == 0:
                grid[x][y] = 1
            else:
                continue

            if x == target_x and y == target_y:
                heapq.heappush(results, (c_path_length, x, y))
            
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx <= target_x and 0 <= ny <= target_y and grid[nx][ny] == 0:
                        queue.append((c_path_length + 1, nx, ny))
        
        if results:
            return heapq.heappop(results)[0]
        return -1