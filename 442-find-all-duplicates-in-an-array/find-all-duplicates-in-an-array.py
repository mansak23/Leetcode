class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for val,freq in count.items():
            if freq>=2:
                res.append(val)
        return res