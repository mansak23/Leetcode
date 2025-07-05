class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        # for i in range (len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             res.append(i)
        #             res.append(j)
        #             return res
        # return res
        m={}#dictionary to store index
        for i,num in enumerate(nums):
            com=target-num
            if com in m:
                return [m[com],i]
            m[num]=i