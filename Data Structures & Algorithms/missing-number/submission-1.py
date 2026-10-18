class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_sum = 0
        total = 0
        i = 0
        for num in nums:
            num_sum += num
            total += i
            i += 1
        total += i
        return total - num_sum
