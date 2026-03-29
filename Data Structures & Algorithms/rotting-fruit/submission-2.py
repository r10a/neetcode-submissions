class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queues = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue = deque()
                    queue.append((x, y))
                    queues.append(queue)
        
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        elapsed = 0
        while True:
            # for row in grid:
            #     print(row)
            # print(elapsed)
            changed = False
            for queue in queues:
                for _ in range(len(queue)):
                    # print(queue)
                    x, y = queue.popleft()
                    for dx, dy in neighbors:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            changed = True
                            # print(changed)
                            queue.append((nx, ny))
            # print()
            # filter empty queues
            queues = [queue for queue in queues if queue]
            if not queues:
                break
            if changed:
                elapsed += 1
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return -1
        
        return elapsed