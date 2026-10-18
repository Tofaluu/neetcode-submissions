from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def recursive(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[i], nums[0])
            else:
                return max(recursive(i - 1), nums[i] + recursive(i - 2))
        
        return recursive(len(nums) - 1)
            
        