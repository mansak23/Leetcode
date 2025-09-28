class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            sub=nums[i:i+3]
            if (sub[0]+sub[1]>sub[2]) and (sub[0]+sub[2]>sub[1]) and (sub[2]+sub[1]>sub[0]):
                return sum(sub)
        return 0