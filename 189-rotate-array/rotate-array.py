class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k==0 or n==1:
            return
        elif k>n:
            k=k%n
        res=nums[-k:]+nums[:n-k]
        nums[:]=res