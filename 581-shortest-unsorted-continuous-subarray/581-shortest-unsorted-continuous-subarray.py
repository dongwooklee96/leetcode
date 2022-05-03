class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start, end = 0, 0

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sorted_nums[i]:
                end = i
                break

        if not start and not end:
            return 0
        return end - start + 1
        

        