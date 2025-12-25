class Solution:
    def maximumHappinessSum(self, hp: List[int], k: int) -> int:
        if k==1:
            return max(hp)
        hp=sorted(hp,reverse=True)
        hp=hp[:k]
        s=0
        for i in range(len(hp)):
            if hp[i]-i >= 0:
                s+=hp[i]-i
        print(hp,s)
        return s