class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        cnt=0
        c=sorted(count.items(),key=lambda x:x[1],reverse=True)
        mx=c[0][1]
        print(mx)
        for num,freq in count.items():
            if freq==mx:
                cnt+=freq
        return cnt