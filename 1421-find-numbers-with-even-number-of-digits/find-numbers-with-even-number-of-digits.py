class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt=0
        for i in nums:
            n=str(i)
            if(len(n)%2==0):
                cnt+=1
        return cnt