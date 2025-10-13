class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[]
        res.append(words[0])
        for i in range(1,len(words)):
            if sorted(words[i])!=sorted(res[-1]):
                res.append(words[i])
        return res