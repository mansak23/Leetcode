class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[0]*(len(nums))
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                res[j]=nums[i]
                j+=1
        nums[:]=res