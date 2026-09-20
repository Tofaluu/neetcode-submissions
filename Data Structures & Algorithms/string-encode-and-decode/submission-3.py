class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        pattern = " "
        for string in strs:
            encoded += string
            pattern += str(len(string)) + ","
        return encoded + pattern
    def decode(self, s: str) -> List[str]:
        pattern = []
        decoded = []
        current_int = ""
        i = len(s) - 1
        while s[i] != " ":
            if s[i] == ",":
                if current_int != "":
                    pattern.append(int("".join(reversed(current_int))))
                current_int = ""
            else:
                current_int += s[i]
            i -= 1
        if current_int != "":
            pattern.append(int("".join(reversed(current_int))))
        for num in reversed(pattern):
            decoded.append(s[0:num])
            if len(s) >= num + 1:
                s = s[num:len(s)]
        return decoded
            

            