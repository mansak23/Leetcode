class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        spl=s.split()
        let=list(pattern)
        if len(set(let))!=len(set(spl)):
            return False
        if len(pattern)!=len(spl):
            return False
        dict={}
        for i in range (len(pattern)):
            if pattern[i] not in dict:
                dict[pattern[i]]=spl[i]
            elif pattern[i] in dict and dict[pattern[i]]==spl[i]:
                continue
            else:
                return False
        print(dict)
        return True