class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx=max(nums)
        c=Counter(nums)
        if c[mx]!=2 or len(nums)!=mx+1:
            return False
        for num,freq in c.items():
            if freq>1 and num!=mx:
                return False
        return True