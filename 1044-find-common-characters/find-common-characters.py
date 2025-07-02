class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count=0
        n=len(words)
        res=[]
        k=0

        for i in range(len(words[0])):
            ch=words[0][i]
            count=0
            for j in range(1,len(words)):
                if ch in words[j]:
                    count+=1
                    words[j]=words[j].replace(ch,"",1)
            if count==(n-1):
                res.append(ch)
        return res