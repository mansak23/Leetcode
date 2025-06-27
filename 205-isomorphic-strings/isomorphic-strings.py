class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict={}
        newt=""
        for i in range(0,len(s)):
            dict[s[i]]=t[i]
        for i in range(0,len(s)):
            newt+=dict[s[i]]
        dup=list(dict.values())
        dupset=set(dup)
        if len(dup)!=len(dupset):
            return False
        if newt==t:
            return True
        return False