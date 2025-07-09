class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            m=bin(i)
            count=Counter(m)
            res.append(count["1"])
        return res