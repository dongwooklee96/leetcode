# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stacks = []
        def recur(node):
            if not node:
                return
            recur(node.left)
            stacks.append(node.val)
            recur(node.right)
        recur(root)
        
        for i in range(len(stacks) - 1):
            if stacks[i] < stacks[i + 1]:
                continue
            else:
                return False
        return True 