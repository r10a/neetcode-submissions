class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.empty = Node(-1, -1)
        self.backing_array = [self.empty] * 1000
        self.capacity = capacity
        self.length = 0
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.right = self.right
        self.right.left = self.left

    def get(self, key: int) -> int:
        node = self.backing_array[key]
        if node == self.empty:
            return self.empty.val
        # already at the end
        if node == self.right.left:
            return node.val
        # detach from current position
        prev = node.left
        next = node.right
        prev.right = next
        next.left = prev
        # move to end
        last_entry = self.right.left
        last_entry.right = node
        node.right = self.right
        node.left = last_entry
        self.right.left = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.backing_array[key] == self.empty:
            self.length += 1
            node = Node(key, value)
            self.backing_array[key] = node
            # add to end
            last_entry = self.right.left
            last_entry.right = node
            node.right = self.right
            node.left = last_entry
            self.right.left = node
        else:
            # detach current position
            node = self.backing_array[key]
            node.val = value
            prev = node.left
            next = node.right
            prev.right = next
            next.left = prev
            # move to end
            last_entry = self.right.left
            last_entry.right = node
            node.right = self.right
            node.left = last_entry
            self.right.left = node

        if self.length > self.capacity:
            to_delete = self.left.right
            # delete from hash
            self.backing_array[to_delete.key] = self.empty
            # delete from dll
            self.left.right = to_delete.right
            to_delete.right.left = self.left
            self.length -= 1
            del to_delete