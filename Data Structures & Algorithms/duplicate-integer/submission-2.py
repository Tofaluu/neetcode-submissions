class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_hm = {}
        for i in nums:
            if i in unique_hm:
                return True
            unique_hm[i] = True
        return False
