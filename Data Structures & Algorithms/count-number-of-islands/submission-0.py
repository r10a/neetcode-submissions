class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        num_islands = 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def explore(x, y):
            queue = deque()
            queue.append((x, y))
            while queue:
                cx, cy = queue.popleft()
                if visited[cx][cy] == 1:
                    continue
                else:
                    visited[cx][cy] = 1
                for ix, iy in neighbors:
                    new_x = cx + ix
                    new_y = cy + iy
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                        queue.append((new_x, new_y))


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # already visited done
                if visited[x][y] == 1:
                    continue
                if grid[x][y] == '1':
                    num_islands += 1
                    explore(x, y)
        
        return num_islands