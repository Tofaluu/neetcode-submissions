class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = 0
        backward = len(s) - 1
        while (forward < backward):
            if not s[forward].isalnum():
                forward += 1
            elif not s[backward].isalnum():
                backward -= 1
            elif s[forward].lower() != s[backward].lower():
                return False
            else:
                forward += 1
                backward -= 1
        return True