class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue_start = deque()
        queue_end = deque()
        target_x, target_y = len(grid) - 1, len(grid[0]) - 1
        queue_start.append((0, 0))
        queue_end.append((target_x, target_y))
        if grid[0][0] != 0 or grid[target_x][target_y] != 0:
            return -1

        grid[0][0] = -1
        grid[target_x][target_y] = -2
        
        start = -1
        end = -2
        path_length = 2
        while queue_start and queue_end:
            for i in grid:
                print(i)
            print()

            for _ in range(len(queue_start)):
                x, y = queue_start.popleft()
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= target_x and 0 <= ny <= target_y:        
                            if grid[nx][ny] == 0:
                                grid[nx][ny] = start
                                queue_start.append((nx, ny))
                            if grid[nx][ny] == end:
                                return path_length
            queue_start, queue_end = queue_end, queue_start
            start, end = end, start
            path_length += 1
        
        return -1