class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        dp=[float('inf')]*(amt+1)
        dp[0]=0
        for i in range(1,amt+1):
            for c in coins:
                if i>=c:
                    dp[i]=min(dp[i],1+dp[i-c])
        return -1 if dp[amt]==float('inf') else dp[amt]