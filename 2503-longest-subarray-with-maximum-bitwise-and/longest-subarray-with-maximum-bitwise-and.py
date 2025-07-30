
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx=max(nums)
        count=0
        longsub=0
        for i in nums:
            if i == mx:
                count+=1
                longsub=max(longsub,count)
            else:
                count=0
        return longsub