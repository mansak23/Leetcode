class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res=nums[0]
        del nums[0]
        nums.sort()
        print(nums[:2])
        res+=sum(nums[:2])
        return res