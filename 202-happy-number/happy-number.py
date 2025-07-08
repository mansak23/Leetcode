class Solution:
    def isHappy(self, n: int) -> bool:
        s=str(n)
        num=0
        if n==7:return True
        while len(s)!=1 or s=="7":
            num=0
            for i in range (len(s)):
                num=num+(int(s[i])**2)
            s=str(num)
        if s=="1":
            return True
        return False
