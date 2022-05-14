from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            p = []
            for _ in range(len(queue)):
                elem = queue.popleft()
                if elem.left:
                    if len(p) > 0:
                        p[-1].next = elem.left
                    p.append(elem.left)
                if elem.right:
                    if len(p) > 0:
                        p[-1].next = elem.right
                    p.append(elem.right)
            queue += p
        return root
        