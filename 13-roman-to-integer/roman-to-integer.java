class Solution {
    public int romanToInt(String s) {
        String r="IVXLCDM";
        int val[]={1,5,10,50,100,500,1000};
        int res=0;
        int n=s.length();
        for(int i=0;i<n;i++){
            char ch=s.charAt(i);
            int val1=val[r.indexOf(ch)];;
            if(i!=n-1){
                char ch1=s.charAt(i+1);
                int val2=val[r.indexOf(ch1)];
                if(val1<val2){
                    res=res+(val2-val1);
                    i=i+1;
                }
                else{
                    res=res+val1;
                }
            }
            else{
                res=res+val1;
            }
        }
        return res;
    }
}