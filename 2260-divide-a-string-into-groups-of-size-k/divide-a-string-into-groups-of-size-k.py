class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        i=0
        n=len(s)
        while(i<n):
            if (i+k)<len(s):
                res.append(s[i:i+k])
            else:
                res.append(s[i:])
            i=i+k
        if(len(res[-1])==k):
            return res
        else:
            for i in range(len(res[-1]),k):
                res[-1]+=fill
        return res
        
            