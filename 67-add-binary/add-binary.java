import java.math.*;
class Solution {
    public String addBinary(String a, String b) {
        BigInteger adec=new BigInteger(a,2);
        BigInteger bdec=new BigInteger(b,2);
        BigInteger res=adec.add(bdec);
        return res.toString(2);
    }
}