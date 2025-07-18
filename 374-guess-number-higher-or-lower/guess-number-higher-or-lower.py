# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        mid=0
        while(left<=right):
            mid=(left+right)//2
            print(mid,left,right)
            if(guess(mid)==0):
                return mid
            elif(guess(mid)==-1):
                right=mid-1
            elif(guess(mid)==1):
                left=mid+1
        return mid
