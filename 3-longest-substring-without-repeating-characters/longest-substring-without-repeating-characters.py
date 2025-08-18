class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=""
        mx=0
        for i in range(len(s)):
            sub=""
            sub+=s[i]
            for j in range(i+1,len(s)):
                if s[j] in sub:
                    break
                else:
                    sub+=s[j]
                # print(sub)
            mx=max(mx,len(sub))
        return mx