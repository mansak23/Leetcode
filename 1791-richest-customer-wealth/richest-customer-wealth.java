class Solution {
    public int maximumWealth(int[][] accounts) {
        int pmax=0,cmax=0;
        for(int i=0;i<accounts.length;i++){
            cmax=0;
            for(int j=0;j<accounts[0].length;j++){
                cmax+=accounts[i][j];
                if(pmax<cmax){
                    pmax=cmax;
                }
            }
        }
        return pmax;
    }
}