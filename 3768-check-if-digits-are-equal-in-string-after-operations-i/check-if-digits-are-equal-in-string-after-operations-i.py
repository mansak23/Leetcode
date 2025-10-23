class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            res=""
            for i in range(len(s)-1):
                res+=str((int(s[i])+int(s[i+1]))%10)
            s=res
        return len(set(s))==1