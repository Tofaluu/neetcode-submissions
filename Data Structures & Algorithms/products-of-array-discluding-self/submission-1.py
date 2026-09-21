class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_total = 1
        zero_count = 0
        solution = []
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product_total *= num
        if zero_count >= 2:
            for num in nums:
                solution.append(0)
        elif zero_count == 1:
            for num in nums:
                if num != 0:
                    solution.append(0)
                else:
                    solution.append(product_total)
        else:
            for num in nums:

                solution.append(product_total // num)

        return solution