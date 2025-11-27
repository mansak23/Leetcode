class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            digit=((list(str(i))))
            if '0' not in digit:
                if all(i%(int(j))== 0 for j in digit):
                    res.append(i)
        return res