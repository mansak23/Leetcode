class Solution:
    def sortVowels(self, s: str) -> str:
        vwl=['a','e','i','o','u','A','E','I','O','U']
        srt=[i for i in s if i in vwl]
        srt.sort()
        res=""
        j=0
        for i in s:
            if i in vwl:
                res+=srt[j]
                j+=1
            else:
                res+=i
        return res