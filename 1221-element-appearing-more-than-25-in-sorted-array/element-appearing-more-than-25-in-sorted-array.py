class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        max=len(arr)//4
        print(max)
        count=Counter(arr)
        for num,freq in count.items():
            if freq>max:
                return num
        return 0