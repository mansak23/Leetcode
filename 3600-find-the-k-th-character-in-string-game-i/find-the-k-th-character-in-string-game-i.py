class Solution:
    def kthCharacter(self, k: int) -> str:
        init="a"
        while(len(init)<k):
            for i in init:
                init+=chr(ord(i)+1)
        print(init)
        return init[k-1]