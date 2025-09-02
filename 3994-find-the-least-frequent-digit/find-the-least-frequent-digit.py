class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s=str(n)
        c=list(s)
        c.sort()
        count=Counter(c)
        count=sorted(count.items(),key=lambda x:x[1])

        return int(count[0][0])