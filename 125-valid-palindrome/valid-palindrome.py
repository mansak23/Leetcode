class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str=re.sub(r'[^a-zA-Z0-9]','',s).lower()
        print(str)
        rev=str[::-1]
        if(str==(rev)):
            return True
        return False
        