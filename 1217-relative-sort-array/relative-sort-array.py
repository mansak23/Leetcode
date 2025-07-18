class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        count=Counter(arr1)
        for i in arr2:
            res+=[i]*count[i]
        arr1.sort()
        for i in arr1:
            if i not in arr2:
                res.append(i) 
        return res