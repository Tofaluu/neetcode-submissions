class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        length = len(s)

        for i in range(length):
            count += 1
            left = i - 1
            right = i + 1
            while (left > -1 and right < length and s[left] == s[right]):
                count += 1
                left -= 1
                right += 1

            left = i
            right = i + 1
            while (left > -1 and right < length and s[left] == s[right]):
                count += 1
                left -= 1
                right += 1
        return count
