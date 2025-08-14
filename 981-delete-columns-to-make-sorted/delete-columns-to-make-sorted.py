class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt=0
        n=len(strs[0])
        m=len(strs)
        for i in range(n):
            for j in range(m-1):
                if strs[j][i]>strs[j+1][i]:
                    # print(strs[j][i],strs[j+1][i])
                    cnt+=1
                    break
        return cnt