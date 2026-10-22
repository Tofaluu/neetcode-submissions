class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        s1_len = len(s1)
        s2_len = len(s2)
        count1 = [0] * 26
        count2 = [0] * 26
        left = 0
        right = 0

        if s1_len > s2_len:
            return False
        
        for i in range(s1_len):
            count1[ord(s1[i]) - 97] += 1
        
        while right < s1_len: 
                count2[ord(s2[right]) - 97] += 1
                right += 1
        
        if count1 == count2:
            return True

        while right < s2_len:
            count2[ord(s2[right]) - 97] += 1
            right += 1
            count2[ord(s2[left]) - 97] -= 1
            left += 1
            if count1 == count2:
                return True



        return False
            

