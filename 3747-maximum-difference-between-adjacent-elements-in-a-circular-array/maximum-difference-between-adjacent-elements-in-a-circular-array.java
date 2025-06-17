class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int max=0,min;
        for(int i=0;i<nums.length;i++){
            if(i==nums.length-1){
                min=Math.abs(nums[i]-nums[0]);
            }
            else{
                min=Math.abs(nums[i]-nums[i+1]);
            }
            if(max<min){
                max=min;
            }
        }
        return max;
    }
}