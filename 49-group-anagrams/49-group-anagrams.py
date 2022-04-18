from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for str in strs:
            hashmap["".join(sorted(str))].append(str)
        return hashmap.values()

            
            
        