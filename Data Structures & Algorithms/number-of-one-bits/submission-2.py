class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        def highestBinary(n):
            num = 1
            while num <= n / 2:
                num *= 2
            return num
        while (n > 0):
            count += 1
            n -= highestBinary(n)
        return count
