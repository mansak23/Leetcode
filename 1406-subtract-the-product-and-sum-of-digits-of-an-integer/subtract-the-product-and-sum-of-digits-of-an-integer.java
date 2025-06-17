class Solution {
    public int subtractProductAndSum(int n) {
        int rem,prod=1,add=0;
        while(n>0){
            rem=n%10;
            prod*=rem;
            add+=rem;
            n=n/10;
        }
        return (prod-add);
    }
}