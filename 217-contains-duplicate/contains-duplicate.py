class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # setn=set(nums)
        # if len(nums)!=len(setn):
        #     return True
        # return False


        # 
        
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False