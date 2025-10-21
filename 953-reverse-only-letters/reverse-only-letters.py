class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st=re.sub(r'[^a-zA-Z]',"",s)
        st=st[::-1]
        res=""
        j=0
        for i in s:
            if not i.isalpha():
                res+=i
            elif j < len(st):
                res+=st[j]
                j+=1
        return res