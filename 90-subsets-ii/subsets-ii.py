class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def bck(s,p):
            if p[:] not in res:
                res.append(p[:])
            for i in range (s,len(nums)):
                p.append(nums[i])
                bck(i+1,p)
                p.pop()
        bck(0,[])
        return res