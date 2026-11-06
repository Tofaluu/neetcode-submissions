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
                temp_left = left
                temp_right = right

                for i in range(right - 1, left - 1, -1):
                    new_s += s[i]
                new_s += " "
                right += 1
                left = right
        
        for i in range(right - 1, left - 1, -1):
            new_s += s[i]
        return new_s