class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            elif not stack:
                return False
            elif bracket == ')':
                top = stack.pop()
                if top != '(':
                    return False
            elif bracket == ']':
                top = stack.pop()
                if top != '[':
                    return False
            elif bracket == '}':
                top = stack.pop()
                if top != '{':
                    return False
            else:
                return False
        if not stack:
            return True
        return False
                