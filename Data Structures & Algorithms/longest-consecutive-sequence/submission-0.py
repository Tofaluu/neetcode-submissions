class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = {}
        longest_streak = 0
        for num in nums:
            nums_hash[num] = 1
        
        for num in nums_hash:
            if (num - 1) not in nums_hash:
                streak = 1
                current_num = num + 1
                while (current_num in nums_hash):
                    streak += 1
                    current_num += 1
                if streak > longest_streak:
                    longest_streak = streak
        return longest_streak
