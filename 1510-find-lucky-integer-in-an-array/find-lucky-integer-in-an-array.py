class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count=Counter(arr)
        count=sorted(count.items(),key=lambda x:x[0],reverse=True)
        for num,freq in count:
            if num==freq:
                return num
        return -1