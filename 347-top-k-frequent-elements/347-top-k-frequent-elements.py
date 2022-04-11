class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        result = []
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        sorted_counter = sorted(counter.items(), key = lambda item: item[1], reverse = True)
        for i in range(k):
            result.append(sorted_counter[i][0])
        return result
        
        
        