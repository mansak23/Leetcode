class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in nums:
            if i%2:
                odd.append(i)
            else:
                even.append(i)
        return even+odd