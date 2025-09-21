class Solution:
    def shortestCompletingWord(self, l: str, words: List[str]) -> str:
        l=l.lower()
        l=re.sub(r'[^a-z]','',l)
        words=sorted(words,key=lambda x:len(x))
        for w in words:
            cnt=0
            for i in l:
                if i in w and w.count(i)>=l.count(i):
                    cnt+=1
            if cnt==len(l):
                return w
        return ""