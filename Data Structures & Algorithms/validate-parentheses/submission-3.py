class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for bracket in s:
            if bracket in mapping:
                if not stack or stack.pop() != mapping[bracket]:
                    return False
            elif bracket in '({[':
                stack.append(bracket)
            else:
                return False
            
        if not stack:
            return True
        return False
                