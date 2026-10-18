from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def recursive(arr: tuple, i):
            if i == 0:
                return arr[0]
            elif i == 1:
                return max(arr[1], arr[0])
            else:
                return max(recursive(arr, i - 1), arr[i] + recursive(arr, i - 2))
        
        if len(nums) == 1:
            return nums[0]
        first = tuple(nums[1:])
        second = tuple(nums[:-1])
        length = len(nums) - 2
        return max(recursive(first, length), recursive(second, length))


        