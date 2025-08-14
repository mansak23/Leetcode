class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        diff=0
        findiff=0
        for i in range(len(colors)):
            diff=0
            for j in range(len(colors)-1,i,-1):
                if colors[i]!=colors[j]:
                    diff=abs(j-i)
                    # print(i,j,diff)
                    break
            findiff=max(diff,findiff)
        return findiff