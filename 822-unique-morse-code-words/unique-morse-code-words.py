class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ls="abcdefghijklmnopqrstuvwxyz"
        res=set()
        for i in words:
            wrd=""
            for j in i:
                wrd+=morse[ls.index(j)]
            res.add(wrd)
        return len(res)
                