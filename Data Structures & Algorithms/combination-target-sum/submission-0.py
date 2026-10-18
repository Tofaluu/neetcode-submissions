class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def recursiveStep(currentList, currentSum, nums, target):
            if currentSum == target:
                result.append(currentList[:])
            else:
                for i in range(len(nums)):
                    if (nums[i] + currentSum <= target):
                        currentList.append(nums[i])

                        recursiveStep(currentList, currentSum + nums[i], nums[i : len(nums)], target)
                        currentList.pop()
        
        recursiveStep([], 0, nums, target)
        return result

