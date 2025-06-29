class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=Counter(s)
        n=len(s)
        countofletter=count[letter]
        return int((countofletter/n)*100)