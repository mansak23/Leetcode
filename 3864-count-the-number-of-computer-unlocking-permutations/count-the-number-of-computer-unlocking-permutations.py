class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        def fact(n):
            x=1
            for i in range(2,n+1):
                x*=i
            return x
        for i in range(1,len(complexity)):
            if complexity[i]<=complexity[0]:
                return 0
        n=len(complexity)
        return fact(n-1)%(10**9 + 7)