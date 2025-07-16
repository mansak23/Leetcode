class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt=0
        visited=""
        for i in word:
            if i.islower():
                if (chr(ord(i)-32)in word) and (i not in visited):
                    print(i)
                    cnt+=1
                    visited+=i
        return cnt