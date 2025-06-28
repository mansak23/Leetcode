class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        JAVA SOLUTION
        class Solution {
    public int[] buildArray(int[] nums) {
        int [] ans=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            ans[i]=nums[nums[i]];
        }
        return ans;
    }
    }"""
        res=[]
        for i in range(0,len(nums)):
            res.append(nums[nums[i]])
        return res