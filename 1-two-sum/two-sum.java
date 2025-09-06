class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> ht=new HashMap<>();
        int[] res=new int[2];
        int comp;
        for(int i=0;i<nums.length;i++){
            comp=target-nums[i];
            if( ht.containsKey(comp)){
                res[0]=ht.get(comp);
                res[1]=i;
            }
            ht.put(nums[i],i);
        }
        return res;
    }
}