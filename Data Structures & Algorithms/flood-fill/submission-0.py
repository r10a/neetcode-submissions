class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        queue.append((sr, sc))
        s_color = image[sr][sc]
        graph_height = len(image) - 1
        graph_width = len(image[0]) - 1
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            # print(queue)
            cx, cy = queue.popleft()
            if image[cx][cy] == color:
                continue
            else:
                image[cx][cy] = color
            for x, y in neighbors:
                new_x = cx-x
                new_y = cy-y
                if 0 <= new_x <= graph_height and 0 <= new_y <= graph_width and image[new_x][new_y] == s_color:
                    queue.append((new_x, new_y))
        
        return image


