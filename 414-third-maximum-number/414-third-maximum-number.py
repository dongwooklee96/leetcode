class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if len(nums) < 3:
            return nums[0]
        
        _set = set()
        ret = nums[0]
        cnt = 0
        for n in nums:
            if n in _set:
                continue
            if cnt == 2:
                ret = n
                break
            _set.add(n)
            cnt += 1
        return ret
        