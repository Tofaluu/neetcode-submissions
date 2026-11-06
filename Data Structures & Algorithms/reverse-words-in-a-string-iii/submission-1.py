class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        left = 0
        right = 0
        new_s = ""
        while (right < n):
            if s[right] != " ":
                right += 1
            else:
                new_s += s[left:right][::-1]
                new_s += " "
                right += 1
                left = right
        
        new_s += s[left:right][::-1]
        return new_s