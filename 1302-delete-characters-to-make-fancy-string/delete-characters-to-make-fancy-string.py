class Solution:
    def makeFancyString(self, s: str) -> str:
        res=""
        for i in range (len(s)-2):
            sub=s[i:i+3]
            # print(sub)
            st=set(sub)
            if len(st)!=1:
                res+=s[i]
        res+=s[-2:]
        return res