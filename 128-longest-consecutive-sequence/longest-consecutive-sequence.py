class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setn=set(nums)
        count=0
        mx=0
        nums=sorted(setn)
        print(nums)
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                count+=1
                mx=max(mx,count)
            else:
                count=0
        if len(nums)==0:
            return 0
        return mx+1