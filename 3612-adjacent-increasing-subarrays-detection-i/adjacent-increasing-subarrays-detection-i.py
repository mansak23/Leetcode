class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-k):
            sub1=nums[i:i+k]
            sub2=nums[i+k:i+k+k]
            print(sub1,sub2)
            if (sub1==sorted(sub1) and len(sub1)==len(set(sub1)) and len(sub1)==k) and (sub2==sorted(sub2) and len(sub2)==len(set(sub2)) and len(sub2)==k):
                return True
        return False