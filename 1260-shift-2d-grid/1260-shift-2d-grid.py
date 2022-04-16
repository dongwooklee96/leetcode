import itertools
import collections

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid[0])
        n = len(grid)
        
        flat = []
        for i in grid:
            flat.extend(i)
        
        k = k % len(flat)
        
        flat = flat[-k:] + flat[:-k]
        ret = []
        for i in range(n):
            ret.append(flat[i*m:m*(i+1)])
        return ret
