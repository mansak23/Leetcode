class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        min="z"
        flag=0
        for i in letters:
            if i>target and i<=min:
                min=i
                flag=1
        if flag==0:
            return letters[0]
        return min
        