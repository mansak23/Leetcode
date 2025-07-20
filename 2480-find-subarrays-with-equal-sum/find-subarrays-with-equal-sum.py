class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # sub=[]
        # if len(nums)==2:
        #     return False
        # prevsum=-1
        # for i in range(len(nums)-1):
        #     sub=nums[i:i+2]
        #     currsum=sum(sub)
        #     print(sub)
        #     print(prevsum,currsum)
        #     if prevsum==currsum:
        #         return True
        #     prevsum=currsum
        # return False
        sm=[]
        for i in range(1,len(nums)):
            sm.append(nums[i-1]+nums[i])
        st=set(sm)
        if len(sm)==len(st):
            return False
        return True