class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = []
        total = 0
        for num in nums:
            total += num
            ret.append(total)
        return ret