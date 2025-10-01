class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        res=""
        while i<len(s):
            sub=s[i:i+(2*k)]
            print(sub)
            i=i+(2*k)
            res+=(sub[:k][::-1]+sub[k:])
        return res
