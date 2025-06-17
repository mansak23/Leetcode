class Solution {
    int maxi(int [] arr){
        int m=arr[0];
        for(int i=1;i<arr.length;i++){
            if(m<arr[i]){
                m=arr[i];
            }
        }
        return m;
    }
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        //int max=Arrays.stream(candies).max().getAsInt();
        List<Boolean> res=new ArrayList<>();
        int max=maxi(candies);
        for(int i=0;i<candies.length;i++){
            if((candies[i]+extraCandies)>=max){
                res.add(true);
            }
            else{
                res.add(false);
            }
        }
        return res;
    }
}