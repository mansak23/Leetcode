class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        res=[]
        for i in nums:
            if i%2:
                odd.append(i)
            else:
                even.append(i)
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
        return res