class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        cnt=0
        n=sorted(nums,reverse=True)
        if n[0]>=(2*n[1]):
                return nums.index(n[0])
        # for i in range(len(nums)-1):
        #     if n[i]>=(2*n[i+1]):
        #         return nums.index(n[i])
        return -1
