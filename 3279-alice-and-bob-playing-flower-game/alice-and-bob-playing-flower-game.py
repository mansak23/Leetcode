class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        evenn=n//2
        oddn=(n+1)//2
        evenm=m//2
        oddm=(m+1)//2
        return ((oddn*evenm)+(evenn*oddm))