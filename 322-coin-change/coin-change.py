class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [2**31] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                if coin <= j:
                    dp[j] = min(dp[j], 1+dp[j-coin])

        return dp[amount] if dp[amount] != 2**31 else -1