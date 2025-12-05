class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)-1):
            sub1=nums[:i+1]
            sub2=nums[i+1:]
            if (abs(sum(sub1)-sum(sub2)))%2 == 0:
                cnt+=1
        return cnt