import java.math.*;
class Solution {
    
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean>ls=new ArrayList<>();
        int j=0;
        for(int i:nums){
            j=((j*2)+i)%5;
            ls.add(j==0);
        }
        return ls;
    }
}