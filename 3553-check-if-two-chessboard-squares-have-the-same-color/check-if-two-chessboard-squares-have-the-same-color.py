class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        odd=['a','c','e','g']
        even=['b','d','f','h']
        alphaa,alphab=coordinate1[0],coordinate2[0]
        numa,numb=int(coordinate1[1]),int(coordinate2[1])
        if((alphaa in even and alphab in even )or (alphaa in odd and alphab in odd)):
            if(numa%2 == numb%2):
                return True
        else:
            if(numa%2 != numb%2):
                return True
        return False