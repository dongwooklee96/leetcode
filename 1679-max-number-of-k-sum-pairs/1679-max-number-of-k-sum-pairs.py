from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        h = defaultdict(int)
        
        for num in nums:
            if h[num] > 0:
                h[num] -= 1
                ans += 1
            else:
                h[k - num] += 1
        return ans 
