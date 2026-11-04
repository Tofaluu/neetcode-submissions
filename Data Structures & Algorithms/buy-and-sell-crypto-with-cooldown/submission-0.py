# sell on i means no buying on i + 1
# buy[i] the max profit on day i given that i hold a share
# sell[i] the max profit on day i given that i do not hold a share
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        if n > 1:
            buy[1] = max(buy[0], -prices[1])
            sell[1] = max(buy[0] + prices[1], sell[0])
        for i in range(2, n):
            price = prices[i]

            buy[i] = max(sell[i - 2] - price, buy[i - 1])

            sell[i] = max(buy[i - 1] + price, sell[i - 1])
        
        return max(buy[n - 1], sell[n - 1])



        