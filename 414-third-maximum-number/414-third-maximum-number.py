import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        prio_queue = [item * -1 for item in list(dict.fromkeys(nums))]
        
        heapq.heapify(prio_queue)
        
        
        if len(prio_queue) > 2:
            for _ in range(2):
                heapq.heappop(prio_queue)
        
        
        return prio_queue[0] * -1
        