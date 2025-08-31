class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        fin=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            fin=max(fin,curr)
            # print(curr,fin)
        return fin