class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                if seen[s[i]] >= start:
                    start = seen[s[i]] + 1
            seen[s[i]] = i
            longest = max(longest, i - start + 1)
        return longest