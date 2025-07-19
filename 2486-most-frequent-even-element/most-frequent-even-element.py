class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        res=[]
        for i in nums:
            if i%2==0:
                res.append(i)
        print(res)
        count=Counter(res)
        count=sorted(count.items(),key=lambda x:-x[1])
        if count==[]:
            return -1
        return count[0][0]