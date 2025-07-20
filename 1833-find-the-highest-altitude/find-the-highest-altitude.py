class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr=[0]
        for i in gain:
            arr.append(arr[-1]+i)
        return max(arr)