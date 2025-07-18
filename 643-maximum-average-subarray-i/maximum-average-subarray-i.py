class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sliding window algo
        sw=sum(nums[:k])
        mx=sw
        for i in range(k,len(nums)):
            sw+=nums[i]-nums[i-k]
            mx=max(mx,sw)
        return mx/k