class Solution:
    def is_sorted(self,nums: List[int])->bool:
        for i in range (1,len(nums)):
            if nums[i-1]<nums[i]:
                return False
        return True
    def triangleType(self, nums: List[int]) -> str:
        tri=set(nums)
        if (nums[0]+nums[1]>nums[2] and nums[0]+nums[2]>nums[1] and nums[1]+nums[2]>nums[0]):
            if len(tri)==1:
                return "equilateral"
            elif len(tri)==2:
                return "isosceles"
            elif len(tri)==3:
                return "scalene"
        return "none"
        