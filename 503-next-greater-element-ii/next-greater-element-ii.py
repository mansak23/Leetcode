class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[]
        n=nums*2
        for i in range(0,len(nums)):
            if nums[i]==max(nums):
                res.append(-1)
            else:
                for j in range(i+1,len(n)):
                    if n[j]>nums[i]:
                        res.append(n[j])
                        break
        return res