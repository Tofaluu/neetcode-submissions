class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        jump = 0
        while i < len(nums) - 1:
            if nums[i] > jump:
                jump = nums[i]
            if jump == 0:
                return False
            jump -= 1
            i += 1

        
        return True

