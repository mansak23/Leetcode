class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        evenn=0
        oddn=0
        for i in range(1,n+1):
            if i%2:
                oddn+=1
            else:
                evenn+=1
        evenm=0
        oddm=0
        for i in range(1,m+1):
            if i%2:
                oddm+=1
            else:
                evenm+=1
        return ((oddn*evenm)+(evenn*oddm))