class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for op in ops:
            if str.isdigit(op.lstrip('-')):
                stack.append(int(op))
            else:
                if op == 'C':
                    stack.pop()
                elif op == 'D':
                    stack.append(stack[-1] * 2)
                elif op == '+':
                    stack.append(stack[-2] + stack[-1])
        return sum(stack)
        