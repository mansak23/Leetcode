class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def divisors(num):
            div = []
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    div.append(i)
                    if i != (num // i):
                        div.append(num // i)
            return div
        
        res = 0
        for n in nums:
            d = divisors(n)
            if len(d) == 4:
                res += sum(d)
        
        return res