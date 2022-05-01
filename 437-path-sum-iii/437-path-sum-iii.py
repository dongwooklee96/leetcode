from collections import deque

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        if not root:
            return cnt

        def dfs(node, target):
            if not node:
                return 0
            return (1 if (target - node.val) == 0 else 0) + \
                dfs(node.left, target - node.val) + \
                dfs(node.right, target - node.val)
        queue = deque()
        queue.append(root)
        
        while len(queue) != 0:
            q_size = len(queue)
            
            for _ in range(q_size):
                node = queue.popleft()
                
                cnt += dfs(node, targetSum)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return cnt
            
        