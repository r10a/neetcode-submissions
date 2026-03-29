class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def get_area(x, y):
            queue = deque()
            queue.append((x, y))
            area = 0
            while queue:
                cx, cy = queue.popleft()
                if grid[cx][cy] == 1:
                    area += 1
                    grid[cx][cy] = 0
                else:
                    continue
                for dx, dy in neighbors:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        queue.append((nx, ny))
            return area
                

        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    max_area = max(get_area(x, y), max_area)
        
        return max_area