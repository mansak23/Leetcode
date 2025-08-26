class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        cnt=0
        mx=max(count.values())
        print(mx)
        for num,freq in count.items():
            if freq==mx:
                cnt+=freq
        return cnt