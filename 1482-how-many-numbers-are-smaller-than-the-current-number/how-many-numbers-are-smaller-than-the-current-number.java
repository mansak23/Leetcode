class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int []small=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            int a=nums[i];
            for(int j=0;j<nums.length;j++){
                if(a>nums[j]){
                    small[i]+=1;
                }
            }
        }
        return small;
    }
}