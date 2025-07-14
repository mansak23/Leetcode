class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=list(set(nums))
        n.sort()
        for i in range (len(n)):
            nums[i]=n[i]
        return len(n)
