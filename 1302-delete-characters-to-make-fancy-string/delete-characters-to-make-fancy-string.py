class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        i=2
        while i<n:
            if s[i-2]==s[i-1]==s[i]:
                s=s[:i]+s[i+1:]
                n=n-1
            else:
                i+=1
        return s