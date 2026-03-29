"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque()
        root = Node(node.val)

        queue.append(node)
        visited = {root.val: root}
        while queue:
            existing_node = queue.popleft()
            for neighbor in existing_node.neighbors:
                if neighbor.val not in visited:
                    new_node = Node(neighbor.val)
                    visited[neighbor.val] = new_node
                    queue.append(neighbor)
                visited[existing_node.val].neighbors.append(visited[neighbor.val])


        return root