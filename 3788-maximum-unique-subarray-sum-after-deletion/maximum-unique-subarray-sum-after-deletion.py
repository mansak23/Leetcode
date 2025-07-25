class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums=set(nums)
        ind=0
        nums=sorted(nums)
        for i in nums:
            if i>=0:
                return sum(nums[nums.index(i):])
        return nums[-1]