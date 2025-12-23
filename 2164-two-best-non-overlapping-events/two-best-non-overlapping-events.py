class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        s = [0]*(n+1)

        for i in range(n-1,-1,-1):
            s[i] = max(s[i+1],events[i][-1])
        
        val = [i for i,e,v in events]
        mx = 0
        for i,e,v in events:
            index = bisect_right(val,e)

            mx =max(mx,v + s[index])
        return mx