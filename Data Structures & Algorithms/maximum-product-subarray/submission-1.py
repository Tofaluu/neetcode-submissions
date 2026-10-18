from functools import cache
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = -11
        cur_max = 1
        cur_min = 1

        for i in range(len(nums)):
            if nums[i] < 0:
                temp = cur_max
                cur_max = cur_min
                cur_min = temp
            cur_max = max(nums[i], nums[i] * cur_max)
            cur_min = min(nums[i], nums[i] * cur_min)
            if cur_max > global_max:
                global_max = cur_max
        return global_max
