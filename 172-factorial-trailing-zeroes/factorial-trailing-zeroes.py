class Solution:
    def fact(self,n:int)->int:
        if n==0 or n==1:
            return 1
        else:
            return n*self.fact(n-1)
    def trailingZeroes(self, n: int) -> int:
        cnt=0
        y=self.fact(n)
        while(y>=0):
            rem=y%10
            if rem==0:
                cnt+=1
            else:
                break
            y=y//10
        return cnt