import collections

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights or not heights[0]:
            return 0

        m, n = len(heights), len(heights[0])
        queue = collections.deque([(0, 0)])
        efforts = {(0, 0): 0}
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dx + x, dy + y
                
                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                eff = max(efforts.get((x, y)), abs(heights[nx][ny] - heights[x][y]))
                
                if (nx, ny) in efforts and efforts[(nx, ny)] <= eff:
                    continue

                efforts[(nx, ny)] = eff
                queue.append((nx, ny))

        if (m - 1, n - 1) not in efforts:
            return -1
        return efforts[(m - 1, n - 1)]
        