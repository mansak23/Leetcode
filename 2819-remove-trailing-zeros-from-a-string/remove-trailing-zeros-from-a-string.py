class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        print(num[-1:])
        while(num[-1:]=="0"):
            num=num[:-1]
        return num