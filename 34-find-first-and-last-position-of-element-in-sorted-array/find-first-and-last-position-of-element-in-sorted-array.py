class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            ind1=nums.index(target)
            ind2=len(nums)-(nums[::-1].index(target))-1
        else:
            ind1,ind2=-1,-1
        return [ind1,ind2]