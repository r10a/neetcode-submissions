# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.k = 0
        self.val = -1
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            self.k += 1
            
            if self.k == k:
                self.val = node.val
            
            inorder(node.right)
        
        inorder(root)
        return self.val