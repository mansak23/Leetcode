class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        a="-"
        rev=""
        if s[0]=='-':
            rev=s[::-1]
            rev=rev[:-1]
            rev="-"+rev
        else:
            rev=s[::-1]
        rev=int(rev)
        if (rev>2**31 - 1 or rev<(-2**31)):
            return 0
        return rev
                