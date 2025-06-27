class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        scount=Counter(s)
        tcount=Counter(t)
        if scount==tcount:
            return True
        return False