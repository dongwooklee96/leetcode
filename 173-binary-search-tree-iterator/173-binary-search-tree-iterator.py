from typing import Optional

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.node = root
        self.stack = []

    def next(self) -> int:
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        u = self.stack.pop()
        self.node = u.right
        return u.val
        

    def hasNext(self) -> bool:
        return self.node or self.stack
