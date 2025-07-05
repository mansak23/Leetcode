class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # setn=set(nums)
        # if len(nums)!=len(setn):
        #     return True
        # return False
        count=Counter(nums)
        print(count)
        for i in count:
            if(count[i]>1):
                return True
        return False