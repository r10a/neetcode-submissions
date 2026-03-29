class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def explore(x, y):
            queue = deque()
            queue.append((x, y))
            while queue:
                cx, cy = queue.popleft()
                if grid[cx][cy] == '1':
                    grid[cx][cy] = '0'
                else:
                    continue
                for ix, iy in neighbors:
                    new_x = cx + ix
                    new_y = cy + iy
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                        queue.append((new_x, new_y))


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    num_islands += 1
                    explore(x, y)
        
        return num_islands