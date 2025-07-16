class Solution:
    def countAsterisks(self, s: str) -> int:
        ind=[]
        i=0
        if "|" not in s:
            c=Counter(s)
            return c['*']
        for i in range(len(s)):
            if s[i]=="|":
                ind.append(i)
        print(ind)
        spl=s[:ind[0]]
        i=2
        while(i<len(ind)):
            spl+=s[ind[i-1]+1:ind[i]]
            i+=2
        spl+=s[ind[-1]+1:]
        count=Counter(spl)
        return count['*']
