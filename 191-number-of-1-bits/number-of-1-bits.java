class Solution {
    public int hammingWeight(int n) {
        int count=0;
        StringBuilder s=new StringBuilder();
        while(n>0){
            s.append(n%2);
            n=n/2;
        }
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='1'){
                count++;
            }
        }
        return count;
    }
}