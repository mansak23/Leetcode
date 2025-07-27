class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hill=0
        valey=0
        n=[]
        n.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]!=n[-1]:
                n.append(nums[i])
        print(n)
        for i in range(1,len(n)-1):
            if n[i-1]<n[i] and n[i+1]<n[i]:
                    hill+=1
            elif n[i-1]>n[i] and n[i+1]>n[i]:
                    valey+=1
        return hill+valey