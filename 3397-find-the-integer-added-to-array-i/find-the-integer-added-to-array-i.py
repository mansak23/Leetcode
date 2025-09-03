class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1==nums2:
            return 0
        k=set()
        nums1=sorted(nums1,reverse=True)
        nums2=sorted(nums2,reverse=True)
        for i in range(len(nums1)):
            k.add(nums2[i]-nums1[i])
        k=list(k)
        return k[0]