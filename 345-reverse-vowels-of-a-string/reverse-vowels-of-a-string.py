class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=['a','e','i','o','u','A','E','I','O','U']
        rev=[s[i] for i in range(len(s)-1,-1,-1) if s[i] in vowel]
        res=""
        j=0
        print(rev)
        for i in s:
            if i in vowel:
                res+=rev[j]
                j+=1
            else:
                res+=i
        return res