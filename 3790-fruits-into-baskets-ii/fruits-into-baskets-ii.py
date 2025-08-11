class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt=0
        for i in fruits:
            for j in range(len(baskets)):
                if baskets[j]>=i:
                    cnt+=1
                    del baskets[j]
                    break
        return len(fruits)-cnt