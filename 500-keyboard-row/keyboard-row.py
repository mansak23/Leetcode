class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        key = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        
        res = []
        for w in words:
            lower_word = w.lower()
            if any(all(ch in r for ch in lower_word) for r in key):
                res.append(w)
        
        return res