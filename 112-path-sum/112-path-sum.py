# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, cur, target):
            
            if not node:
                return False
            
            if not node.left and not node.right:
                if node.val + cur == target:
                    return True
                return False
            return (dfs(node.left, cur + node.val, target) or
                    dfs(node.right, cur + node.val, target))
        return dfs(root, 0, targetSum)
        