class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        cnt=0
        num=floor(n/(1/x))
        res=[]
        for i in range(1,num+1):
            res.append(i**x)
        print(res)
        dp=[0]*(n+1)
        dp[0]=1
        for i in res:
            for s in range(n,i-1,-1):
                dp[s]+=dp[s-i]
        return dp[n]%(10**9+7)