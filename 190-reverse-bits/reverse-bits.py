class Solution:
    def reverseBits(self, n: int) -> int:
       num=bin(n)
       num=num[2:]
       l=32-len(num)
       num='0'*l+num
       num=num[::-1]
       return int(num,2)