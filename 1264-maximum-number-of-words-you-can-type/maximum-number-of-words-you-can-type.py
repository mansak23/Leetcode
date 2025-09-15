class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt=0
        ls=text.split()
        ltr=list(brokenLetters)
        for i in ls:
            if all(l not in i for l in ltr):
                cnt+=1
        return cnt