class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # mx=max(nums)
        # if -mx in nums:
        #     return mx
        # for i in range(len(nums)):
        #     nums.remove(mx)
        #     if nums!=[]:
        #         mx=max(nums)
        #     if -mx in nums:
        #         return mx
        # return -1
        nums=set(nums)
        nums=sorted(nums)
        print(nums)
        for i in nums:
            if -i in nums:
                return -i
        return -1