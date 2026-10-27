class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            margin = prices[i] - lowest_price
            if margin > max_profit:
                max_profit = margin
            if margin < 0:
                lowest_price = prices[i]
        return max_profit
