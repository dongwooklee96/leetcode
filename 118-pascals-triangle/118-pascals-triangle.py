class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        if numRows <= 0:
            return pascal
        pascal.append([1])
        
        for i in range(1, numRows):
            prev_list = pascal[i - 1]
            curr_list = []
            for j in range(len(prev_list) + 1):
                if 0 < j < len(prev_list):
                    curr_list.append(prev_list[j - 1] + prev_list[j])
                    continue
                curr_list.append(1)
                
            pascal.append(curr_list)
        
        return pascal
        