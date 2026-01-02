class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)/2
        c=Counter(nums)
        for e,f in c.items():
            if f==n:
                return e