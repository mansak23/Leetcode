class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        cnt=nb
        while nb>=0:
            if (nb//ne)==0:
                break
            cnt+=nb//ne
            rem=nb%ne
            nb=(nb//ne)+rem
        return cnt
