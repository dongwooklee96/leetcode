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
        