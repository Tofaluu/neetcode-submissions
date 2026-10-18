from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def recursive(string):
            if string == "":
                return 1
            elif string[0] == "0":
                return 0
            elif len(string) == 1:
                return 1
            else:
                if int(string[0:2]) > 26:
                    return recursive(string[1:])
                return recursive(string[1:]) + recursive(string[2:])
        return recursive(s)