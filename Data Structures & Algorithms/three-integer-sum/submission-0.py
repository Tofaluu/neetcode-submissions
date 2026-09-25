class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        solution = []
        for i in range(length - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = length - 1
            while (low < high):
                sum = nums[i] + nums[low] + nums[high]
                if sum > 0:
                    high -= 1
                elif sum < 0:
                    low += 1
                else:
                    solution.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while (low < length and nums[low] == nums[low - 1]):
                        low += 1
                    while (high > i and nums[high] == nums[high + 1]):
                        high -= 1
        return solution

        