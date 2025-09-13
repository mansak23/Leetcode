class Solution:
    def maxFreqSum(self, s: str) -> int:
        vwl="aeiou"
        cnst="bcdfghjklmnpqrstvwxyz"
        vn=0
        cn=0
        flagc,flagv=True,True
        cc=0
        count=Counter(s)
        count=sorted(count.items(),key=lambda x:x[1],reverse=True)
        for char,freq in count:
            if char in cnst and flagc:
                cn=freq
                flagc=False
                cc+=1
            elif char in vwl and flagv:
                vn=freq
                flagv=False
                cc+=1
            if cc==2:
                break
        return vn+cn