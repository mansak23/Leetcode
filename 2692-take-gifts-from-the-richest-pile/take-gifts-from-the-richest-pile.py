class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            mx=max(gifts)
            ind=gifts.index(mx)
            gifts[ind]=int(sqrt(mx))
        return sum(gifts)