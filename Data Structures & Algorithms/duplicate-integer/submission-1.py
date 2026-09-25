class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for i in nums:
            if i in unique_set:
                return True
            unique_set.add(i)
        return False
