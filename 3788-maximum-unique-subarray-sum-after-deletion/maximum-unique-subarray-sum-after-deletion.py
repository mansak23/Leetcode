class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=sorted(nums)
        total=sum(nums)
        for i in range (0,len(nums)):
            print(nums[i:])
            sub=sum(nums[i:])
            print(sub)
            if sub>total:
                total = sub
        return total