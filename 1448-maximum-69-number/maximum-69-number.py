class Solution:
    def maximum69Number (self, num: int) -> int:
        n=str(num)
        # ind=n.index(6)
        n=n.replace('6','9',1)
        return int(n)