class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        answer = []
        n = len(nums) + 1
        order = [None] * n
        for integer in nums:
            if integer in num_counts:
                num_counts[integer] += 1
            else:
                num_counts[integer] = 1
        
        for integer in num_counts:
            if order[num_counts[integer]] != None:
                order[num_counts[integer]].append(integer)
            else:
                order[num_counts[integer]] = [integer]

        for bucket in reversed(order):
            if bucket != None:
                for integer in bucket:
                    answer.append(integer)
                    k -= 1
                if k <= 0:
                    return answer