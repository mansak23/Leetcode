class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        fiveperc=int(n/20)
        arr.sort()
        arr=arr[fiveperc:-fiveperc]
        return mean(arr)