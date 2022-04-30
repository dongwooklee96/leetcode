class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solution(nums, subset, i, answer):
            ret = []
            if len(nums) == i:
                for i, v in enumerate(nums):
                    if subset[i]:
                        ret.append(v)
                answer.append(ret)
                return
            subset[i] = False
            solution(nums, subset, i + 1, answer)
            subset[i] = True
            solution(nums, subset, i + 1, answer)

        answer = []
        subset = [False] * len(nums)
        solution(nums, subset, 0, answer)
        return answer
        
        
        
            
            
    
    
        
        
    
        
        
        