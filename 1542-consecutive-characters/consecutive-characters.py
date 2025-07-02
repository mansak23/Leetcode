class Solution:
    def maxPower(self, s: str) -> int:
        count=0
        mx=0
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count+=1
            mx=max(mx,count)
            if s[i-1]!=s[i]:
                count=0
        return mx+1