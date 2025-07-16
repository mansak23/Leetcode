class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum=0
        pref={0:1}
        cnt=0
        for i in nums:
            prefixsum+=i
            if prefixsum-k in pref:
                cnt+=pref[prefixsum-k]
            pref[prefixsum]=pref.get(prefixsum,0)+1
        print(pref)
        return cnt