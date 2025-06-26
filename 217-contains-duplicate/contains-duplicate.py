class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nm=set(nums)
        # print(nm)
        # if(len(nums)==len(nm)):
        #     return 
        # return True
        count=Counter(nums)
        print(count)
        for i in count:
            if(count[i]>1):
                return True
        return False