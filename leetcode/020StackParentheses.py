# 40 ms, faster than 55.07% of Python3
class Solution:
    def isValid(self, s: str) -> bool:
        # stack, list append or pop
        stack = []
        matches = {'(':')', '{':'}','[':']'}
        
        for each in s:
            if each in matches.keys():
                stack.append(each)
            elif each in matches.values():
                if stack == [] or each != matches[stack.pop()]:
                    return False
            else: return False    
        return stack == []
