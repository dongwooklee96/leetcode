class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for idx, num in enumerate(nums):
            if dictionary.get(target - num) is not None:
                return [idx, dictionary.get(target - num)]
            else:
                dictionary[num] = idx
            
        