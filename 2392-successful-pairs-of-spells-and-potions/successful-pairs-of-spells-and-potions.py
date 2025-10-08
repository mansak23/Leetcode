class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res=[]
        potions.sort()
        print(potions)
        for i in spells:
            left=0
            right=len(potions)-1
            ind=len(potions)
            while left<=right:
                mid=(left+right)//2
                if potions[mid]*i>=success:
                    ind=mid
                    right=mid-1
                else:
                    left=mid+1
            res.append(len(potions)-ind)
        return res