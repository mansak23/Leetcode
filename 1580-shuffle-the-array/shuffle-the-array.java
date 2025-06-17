class Solution {
    public int[] shuffle(int[] nums, int n) {
            int j=0;
            int [] ans=new int[2*n];
            for(int i=0;i<n;i++){
                ans[j]=nums[i];
                j++;
                if(i+n < n*2){
                    ans[j]=nums[i+n];
                    j++;
                }
            }
            return ans;
    }
}