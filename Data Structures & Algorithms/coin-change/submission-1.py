from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def recursive(amount):
            min_coins = 100000
            if amount < 0:
                return 100000
            elif amount == 0:
                return 0
            else:
                for i in range(len(coins)):
                    if coins[i] <= amount:
                        cost = 1 + recursive(amount - coins[i])
                        min_coins = min(cost, min_coins)
                return min_coins
        min_coin = recursive(amount)
        if min_coin > 10000:
            return -1
        else:
            return min_coin

                    
                    
