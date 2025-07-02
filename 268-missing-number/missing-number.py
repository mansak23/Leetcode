class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        print(nums)
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]-1:
                return nums[i]-1
        if len(nums) not in nums:
            return len(nums)
        return 0