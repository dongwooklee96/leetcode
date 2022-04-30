class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []
        
        for ch in s:
            if ch not in map.keys():
                stack.append(ch)
            else:
                pair = stack.pop() if stack else ''
                if pair != map[ch]:
                    return False
        if len(stack) != 0:
            return False
        return True
                
        