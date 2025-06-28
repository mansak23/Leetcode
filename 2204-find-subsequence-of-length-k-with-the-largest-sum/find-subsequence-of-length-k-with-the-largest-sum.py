class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        withindex=list(enumerate(nums))
        sortenum=sorted(withindex,key=lambda x:x[1],reverse=True)[:k]
        finsort=sorted(sortenum,key=lambda x:x[0])
        print(finsort)
        return [i[1] for i in finsort]
        