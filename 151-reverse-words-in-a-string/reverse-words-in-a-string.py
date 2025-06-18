class Solution:
    def reverseWords(self, s: str) -> str:
        ls=s.split()
        ls.reverse()
        str=" ".join(ls)
        return str