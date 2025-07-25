class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # nums=set(nums)
        # ind=0
        # nums=sorted(nums)
        # for i in nums:
        #     if i>=0:
        #         return sum(nums[nums.index(i):])
        # return nums[-1]
    
        if all(n < 0 for n in nums):
            return max(nums)
        
        unique = set(nums)
        return sum(n for n in unique if n > 0)