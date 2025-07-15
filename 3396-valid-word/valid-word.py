class Solution:
    def isValid(self, word: str) -> bool:
        word1=re.sub(r'[^0-9a-zA-z]',"",word)
        print(word1)
        if len(word)<3 or (len(word1)!=len(word)):
            return False
        word=word.lower()
        vowel=['a','e','i','o','u']
        ccnt=0
        vcnt=0
        justchar=re.sub(r'[^a-z]',"",word)
        for i in justchar:
            if i in vowel:
                vcnt+=1
            else:
                ccnt+=1
        print(vcnt,ccnt)
        if ccnt==0 or vcnt==0:
            return False
        return True