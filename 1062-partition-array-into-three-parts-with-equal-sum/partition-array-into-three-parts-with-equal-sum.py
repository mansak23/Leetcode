class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sm=sum(arr)/3
        print(sm)
        s=0
        count=0
        for i in arr:
            s+=i
            if s==sm:
                count+=1
                s=0
        if count>=3:
            return True
        return False