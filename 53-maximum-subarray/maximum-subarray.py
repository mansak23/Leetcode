class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=nums[0]
        res=nums[0]
        for i in range (1,len(nums)):
            mx=max(mx+nums[i],nums[i])
            res=max(res,mx)
        return res