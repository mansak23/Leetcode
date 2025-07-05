class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setn=set(nums)
        if len(nums)!=len(setn):
            return True
        return False