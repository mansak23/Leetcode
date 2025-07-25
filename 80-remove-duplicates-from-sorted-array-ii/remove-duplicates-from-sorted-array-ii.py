class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=[]
        for i in nums:
            if count[i]<=2:
                res.append(i)
                count[i]-=1
            else:
                count[i]-=1
        nums[:]=res
            