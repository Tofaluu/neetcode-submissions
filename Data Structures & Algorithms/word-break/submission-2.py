from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def recursive(string):
            if string == "":
                return True
            else:
                for i in range(len(string)):
                    if string[:i + 1] in wordDict:
                        if recursive(string[i + 1:]):
                            return True
                return False
        
        return recursive(s)