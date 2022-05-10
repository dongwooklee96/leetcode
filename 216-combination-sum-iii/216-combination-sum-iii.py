from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        items = list(combinations(items, k))
        ans = []
        for item in items:
            if sum(item) == n:
                ans.append(item)
        return ans
        