class Solution {
    public int removeDuplicates(int[] nums) {
        int i=0,j;
        j=1;
        //int flag=0;
        while(j<nums.length && i<nums.length){
            if(nums[i]==nums[j]){
                j++;
            }
            else{
                nums[i+1]=nums[j];
                i++;
            }
        }
        return i+1;
    }
}