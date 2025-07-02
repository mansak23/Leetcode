class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            mx=max(mx,count)
            if nums[i]==0:
                count=0
        return mx