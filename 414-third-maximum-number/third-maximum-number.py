class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=set(nums)
        n=sorted(n)
        n.reverse()
        print(n)
        if len(n)<=2:
            return n[0]
        return n[2]