class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for index,num in enumerate(s):
            if count[num]==1:
                return index
        return -1