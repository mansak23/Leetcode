class Solution:
    def reverseWords(self, s: str) -> str:
        ls=s.split()
        res=""
        for i in ls:
            res+=i[::-1]+" "
        return res[:-1]