class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls=s.split()
        print(ls[-1])
        return len(ls[-1])