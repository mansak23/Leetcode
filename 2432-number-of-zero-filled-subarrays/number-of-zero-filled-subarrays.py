class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt=0
        res=0
        for n in nums:
            if n==0:
                cnt+=1
                res+=cnt
            else:
                cnt=0
        return res