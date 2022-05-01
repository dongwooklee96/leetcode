# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low, high = float('-inf'), float('inf')
        
        def recur(node, high, low):
            if not node:
                return True
            
            if low < node.val < high:
                pass
            else:
                return False
            
            return recur(node.left, node.val, low) and recur(node.right, high, node.val)
        return recur(root, high, low)
            
        
                