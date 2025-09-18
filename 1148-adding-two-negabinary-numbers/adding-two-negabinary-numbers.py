class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n1,j=0,0
        for i in range(len(arr1)-1,-1,-1):
            n1+=((-2)**j)*arr1[i]
            j+=1
        n2,j=0,0
        for i in range(len(arr2)-1,-1,-1):
            n2+=((-2)**j)*arr2[i]
            j+=1
        total=n1+n2
        if total==0:
            return [0]
        res=[]
        while total!=0:
            total,remainder=divmod(total,-2)
            if remainder<0:
                total+=1
                remainder+=2
            res.append(remainder)
        return res[::-1]
