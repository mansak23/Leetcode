class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # sortednums=sorted(nums)
        # i=0
        # while(k!=len(nums)):
        #     nums.remove(sortednums[i])
        #     i+=1
        # return nums
        # using enumerate
        withindex=list(enumerate(nums))
        sortenum=sorted(withindex,key=lambda x:x[1],reverse=True)[:k]
        finsort=sorted(sortenum,key=lambda x:x[0])
        return [i[1] for i in finsort]
        