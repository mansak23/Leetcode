class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dict={}
        for i in range(len(nums)-1):
            if nums[i]==key :
                dict[nums[i+1]]=dict.get(nums[i+1],0)+1
        dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
        return dict[0][0]