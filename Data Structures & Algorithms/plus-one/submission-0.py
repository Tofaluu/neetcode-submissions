# iterate from end of array to start, utilize carry variable?
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        last_digit = digits[n - 1] + 1
        if last_digit == 10:
            digits[n - 1] = 0
            i = n - 2
            carry = 1
            while (carry and i >= 0):
                digit = digits[i] + 1
                if digit == 10:
                    digits[i] = 0
                    i -= 1
                else:
                    digits[i] = digit
                    carry = 0    
            if i == -1:
                return [1] + digits
            

        else:
            digits[n - 1] = last_digit
        return digits

        