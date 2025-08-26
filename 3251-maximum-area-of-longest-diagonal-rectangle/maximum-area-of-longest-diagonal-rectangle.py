class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag=[]
        for i in dimensions:
            diag.append(sqrt((i[0]*i[0])+(i[1]*i[1])))
        mx=max(diag)
        indices=[ind for ind in range(len(diag)) if diag[ind]==mx]
        print(indices)
        if len(indices)!=1:
            r=0
            for i in indices:
                r=max(r,dimensions[i][0]*dimensions[i][1])
            return r
        ind=diag.index(mx)
        return dimensions[ind][0]*dimensions[ind][1]