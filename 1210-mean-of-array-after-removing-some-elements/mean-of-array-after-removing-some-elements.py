class Solution:
    def trimMean(self, arr: List[int]) -> float:
        fiveperc=int(len(arr)/20)
        arr.sort()
        arr=arr[fiveperc:-fiveperc]
        return sum(arr)/len(arr)