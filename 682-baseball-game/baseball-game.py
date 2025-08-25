class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in range(len(operations)):
            if operations[i].lstrip('+-').isdigit():
                res.append(int(operations[i]))
            elif operations[i]=='C':
                del res[-1]
            elif operations[i]=='D':
                res.append(int(res[-1])*2)
            elif operations[i]=='+':
                res.append(int(res[-1])+int(res[-2]))
            print(res)
        return sum(res)