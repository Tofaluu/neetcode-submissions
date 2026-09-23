class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0
        
        for num in nums_set:
            if (num - 1) not in nums_set:
                streak = 1
                current_num = num + 1
                while (current_num in nums_set):
                    streak += 1
                    current_num += 1
                if streak > longest_streak:
                    longest_streak = streak
        return longest_streak
