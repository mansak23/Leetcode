class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        # flag=True
        for i in nums1:
            ind=nums2.index(i)
            flag=True
            print(ind)
            for j in range(ind+1,len(nums2)):
                if nums2[j]>i:
                    res.append(nums2[j])
                    flag=False
                    break
            if flag:
                res.append(-1)
            print(res)
        
        return res