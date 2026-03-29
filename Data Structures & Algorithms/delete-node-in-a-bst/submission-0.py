# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _find_right_most_min(self, node):
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                in_order_successor = self._find_right_most_min(root)
                root.val = in_order_successor.val
                root.right = self.deleteNode(root.right, in_order_successor.val)
        return root