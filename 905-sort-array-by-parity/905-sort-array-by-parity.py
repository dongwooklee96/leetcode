from collections import deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        queue = deque()
        
        for num in nums:
            if num % 2 == 0:
                queue.appendleft(num)
            else:
                queue.append(num)
        return queue 