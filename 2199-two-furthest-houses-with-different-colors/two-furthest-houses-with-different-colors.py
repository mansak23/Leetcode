class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        fin=0
        for i in range(len(colors)):
            diff=0
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    diff=abs(j-i)
            fin=max(fin,diff)
        return fin