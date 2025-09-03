class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        for i in range(min(len(word1),len(word2))):
            res+=word1[i]+word2[i]
        x=word1 if len(word1)>len(word2) else word2
        y=word1 if len(word1)<len(word2) else word2
        res+=x[len(y):]
        return res
        