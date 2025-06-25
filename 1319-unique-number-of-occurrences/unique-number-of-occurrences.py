class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count=Counter(arr)
        ls=count.values()
        s=set(ls)
        if(len(s)==len(ls)):
            return True
        return False