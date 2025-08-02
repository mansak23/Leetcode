class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=[]
        for i in grid:
            for j in i:
                l.append(j)
        print(l)
        c=Counter(l)
        c=sorted(c.items(),key=lambda x:x[1],reverse=True)
        res=[]
        res.append(c[0][0])
        r=l[:]
        l=list(set(l))
        l.sort()
        print(l)
        v=0
        s=[]
        for i in range(1,len(r)+1):
            s.append(i)
        print(s)
        for i in s:
            if i not in l:
                v=i
        res.append(v)
        return res