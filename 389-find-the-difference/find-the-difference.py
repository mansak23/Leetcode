class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        for i in range(0,len(s)):
            if s[i] in t:
                t=t.replace(s[i],"",1)
        print(t)
        return t[0]