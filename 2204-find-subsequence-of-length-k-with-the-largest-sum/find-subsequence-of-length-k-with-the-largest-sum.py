class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sortednums=sorted(nums)
        i=0
        while(k!=len(nums)):
            nums.remove(sortednums[i])
            i+=1
        return nums
        
        