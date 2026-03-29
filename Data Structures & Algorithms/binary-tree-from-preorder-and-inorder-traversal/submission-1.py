# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
                return None
        
        inorder_lookup = { val: idx for idx, val in enumerate(inorder) }

        def traverse(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            
            root = TreeNode(preorder[pl])

            mid = inorder_lookup[root.val]
            left_size = mid - il

            root.left = traverse(pl + 1, pl + left_size, il, mid)
            root.right = traverse(pl + left_size + 1, pr, mid + 1, ir)

            return root
        
        return traverse(0, len(preorder) - 1, 0, len(inorder) - 1)