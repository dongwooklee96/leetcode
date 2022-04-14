# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(node):
    if not node:
        return
    ret.append(node.val)
    traverse(node.left)
    traverse(node.right)

def search(node, val):
    if not node:
        return
    if val == node.val:
        return node
    elif val < node.val:
        return search(node.left, val)
    elif val > node.val:
        return search(node.right, val)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return search(root, val)
        