class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
        dp[1][1] = 1
        for i in range(0, m):
            for j in range(0, n):
                above = dp[i][j + 1]
                left = dp[i + 1][j]
                dp[i + 1][j + 1] += above + left


        return dp[m][n]








