class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        answer = []
        index = 0
        for i in nums:
            needed[target - i] = index
            index += 1
        
        index = 0
        for j in nums:
            if j in needed and index != needed[j]:
                answer.append(index)
                answer.append(needed[j])
                return answer
            index += 1  