import itertools
import collections

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        width = len(grid[0])
        height = len(grid)
        
        deque = collections.deque(list(itertools.chain.from_iterable(grid)))
        
        for i in range(k):
            temp = deque.pop()
            deque.appendleft(temp)
        
        ret = []
        for _ in range(height):
            temp = []
            for _ in range(width):
                temp.append(deque.popleft())
            ret.append(temp)
        return ret
                
                
                
        
        
            
        
        