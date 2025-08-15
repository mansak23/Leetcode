class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        m=log(n,4)
        if 4**(ceil(m))==n:
            return True
        return False
