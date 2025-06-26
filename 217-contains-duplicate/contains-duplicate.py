class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nm=set(nums)
        print(nm)
        if(len(nums)==len(nm)):
            return False
        return True