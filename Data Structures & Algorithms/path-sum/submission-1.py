# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, running_sum):
            if not node.right and not node.left:
                if running_sum == targetSum:
                    return True
                return False
            
            if (node.left and dfs(node.left, running_sum + node.left.val)) or \
                (node.right and dfs(node.right, running_sum + node.right.val)):
                return True
            
            return False
        
        return dfs(root, root.val)