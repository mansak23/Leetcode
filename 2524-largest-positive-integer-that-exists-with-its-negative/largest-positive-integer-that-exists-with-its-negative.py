class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mx=max(nums)
        if -mx in nums:
            return mx
        for i in range(len(nums)):
            nums.remove(mx)
            if nums!=[]:
                mx=max(nums)
            if -mx in nums:
                return mx
        return -1