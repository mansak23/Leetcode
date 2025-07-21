class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count=Counter(nums)
        count=sorted(count.items(),key = lambda x:x[1])
        return count[0][0]
