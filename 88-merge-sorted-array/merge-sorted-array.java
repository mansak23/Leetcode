class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i,j;
        j=m;
        for(i=0;i<n;i++,j++){
            nums1[j]=nums2[i];
        }
        Arrays.sort(nums1);
}
}