class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res=sorted(heights)
        count=0
        for i in range (0,len(res)):
            if heights[i]!=res[i]:
                count+=1
        return count