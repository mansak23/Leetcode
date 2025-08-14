class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # freq=[]
        # for i in range(len(num)-2):
        #     sub=num[i:i+3]
        #     if len(set(sub))==1:
        #         freq.append(sub[0])
        # if freq == []:
        #     return ""
        # return str(max(freq))*3

        for i in range(9,-1,-1):
            if str(i)*3 in num:
                return str(i)*3
        return ""