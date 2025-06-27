class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rc=Counter(ransomNote)
        mc=Counter(magazine)
        for k,v in rc.items():
            if mc[k]<v:
                return False
        return True