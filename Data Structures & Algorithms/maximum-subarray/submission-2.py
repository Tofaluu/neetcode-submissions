class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = nums[0]
        max_count = count
        for i in range(1, len(nums)):
            if nums[i] + count < nums[i]:
                count = nums[i]
            else:
                count += nums[i]
            if count > max_count:
                max_count = count
        return max_count