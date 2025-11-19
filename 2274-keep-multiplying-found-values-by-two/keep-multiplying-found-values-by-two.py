class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        while(True):
            c=original*2
            if c in nums:
                original*=2
            else:
                return c
        