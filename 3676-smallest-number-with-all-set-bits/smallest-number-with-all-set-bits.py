class Solution:
    def smallestNumber(self, n: int) -> int:
        if n<3:
            return n
        setbit=[3]
        while(setbit[-1]<=1000):
            setbit.append(setbit[-1]*2+1)
        print(setbit)
        for i in setbit:
            if i >= n:
                return i
        return -1