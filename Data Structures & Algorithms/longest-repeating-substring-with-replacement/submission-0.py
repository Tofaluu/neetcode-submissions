class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        left = 0
        window = [0] * 26
        best_result = 0

        for right in range(len(s)):
            window[ord(s[right]) - ord('A')] += 1

            while (max(window) + k < right - left + 1):
                window[ord(s[left]) - ord('A')] -= 1
                left += 1

            if (right - left + 1 > best_result):
                best_result = right - left + 1
        return best_result