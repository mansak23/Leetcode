class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mn=201
        for i in tasks:
            mn=min(mn,sum(i))
        return mn