class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            max_prev = 0
            for j in range(0, i):
                if nums[j] < nums[i] and dp[j] > max_prev:
                    max_prev = dp[j]
            dp.append(1 + max_prev)
        
        return max(dp)
