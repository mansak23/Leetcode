class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        a=set()
        for _ in range (len(nums)//2):
            mn=min(nums)
            mx=max(nums)
            nums.remove(mn)
            nums.remove(mx)
            a.add((mn+mx)/2)
        return len(a)