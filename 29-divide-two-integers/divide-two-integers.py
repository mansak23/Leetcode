class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=int(dividend/divisor)
        if res>2**31-1:
            return 2**31-1
        return res