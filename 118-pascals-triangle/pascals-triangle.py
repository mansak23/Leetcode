class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        if numRows==1:
            return res
        res.append([1,1])
        if numRows==2:
            return res
        print(len(res[-1]))
        for _ in range(2,numRows):
            prev=res[-1]
            curr=[1]
            for i in range(0,len(res[-1])-1):
                curr.append(prev[i]+prev[i+1])
            curr.append(1)
            res.append(curr)
        return res