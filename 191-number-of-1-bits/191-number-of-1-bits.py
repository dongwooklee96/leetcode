class Solution:
    def hammingWeight(self, n: int) -> int:
        a = (str(bin(n)))
        return a.count('1')
        