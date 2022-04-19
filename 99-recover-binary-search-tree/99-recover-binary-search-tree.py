# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            node_list.append(node)
            traverse(node.right)

        traverse(root)
        
        idx_list = []
        for idx, sorted_node in enumerate(sorted(node_list, key=lambda node:node.val)):
            if sorted_node.val != node_list[idx].val:
                idx_list.append(idx)
        node_list[idx_list[0]].val, node_list[idx_list[1]].val = node_list[idx_list[1]].val, node_list[idx_list[0]].val