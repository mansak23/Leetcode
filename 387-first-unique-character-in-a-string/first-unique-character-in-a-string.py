class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        for i in s:
            if dict[i]==1:
                return s.index(i)
        return -1