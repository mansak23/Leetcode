class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt=0
        j=0
        prod=1
        for i in range(len(nums)):
            prod*=nums[i]
            while prod>=k and j<=i:
                prod/=nums[j]
                j+=1
            cnt+=i-j+1
        return cnt