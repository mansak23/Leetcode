class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        num=re.sub(r'[^0-9]','',number)
        print(num)
        res=""
        while(len(num)!=0):
            if(len(num)>4):
                res=res+num[0:3]+'-'
                num=num[3:]
            elif len(num)==3:
                res=res+num[0:3]+'-'
                num=num[3:]
            elif len(num)==4:
                res=res+num[0:2]+'-'+num[2:4]
                num=num[4:]
            elif len(num)==2:
                res=res+num[0:2]
                num=num[2:]
        if(res[-1]=='-'):
            res=res[0:len(res)-1]
        return res