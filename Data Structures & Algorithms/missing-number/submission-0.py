class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        total = 0
        i = 0
        for num in nums:
            sum += num
            total += i
            i += 1
        total += i
        return total - sum
