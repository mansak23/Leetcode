class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        srt=sqrt(num)
        srtint=int(sqrt(num))
        if srt-srtint == 0:
            return True
        return False
        