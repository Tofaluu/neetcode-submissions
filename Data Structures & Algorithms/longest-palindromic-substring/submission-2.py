class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        length = len(s)
        for i in range(length):
            oddString = s[i]
            left = i - 1
            right = i + 1
            while (left > -1 and right < length and s[left] == s[right]):
                oddString = s[left] + oddString + s[right]
                left -= 1
                right += 1

            left = i
            right = i + 1
            evenString = ""
            while (left > -1 and right < length and s[left] == s[right]):
                evenString = s[left] + evenString + s[right]
                left -= 1
                right += 1
            
            if max(len(oddString), len(evenString)) > len(longest):
                if len(oddString) > len(evenString):
                    longest = oddString
                else:
                    longest = evenString

        return longest

