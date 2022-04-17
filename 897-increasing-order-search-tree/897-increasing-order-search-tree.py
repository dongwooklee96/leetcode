# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tree_nodes = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            tree_nodes.append(TreeNode(val=node.val))
            traverse(node.right)
        traverse(root)
                        
        for idx, node in enumerate(tree_nodes):
            if idx == len(tree_nodes) - 1:
                break
            node.right = tree_nodes[idx + 1]
        return tree_nodes[0] 
        