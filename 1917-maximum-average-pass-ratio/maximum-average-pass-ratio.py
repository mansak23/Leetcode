class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap=[]
        for p,t in classes:
            gain=((p+1)/(t+1))-(p/t)
            heapq.heappush(max_heap,(-gain,p,t))
        
        for _ in range (extraStudents):
            ng,p,t=heapq.heappop(max_heap)
            p+=1
            t+=1
            newg=((p+1)/(t+1))-(p/t)
            heapq.heappush(max_heap,(-newg,p,t))
        
        res_ratio=0
        while max_heap:
            _,p,t=heapq.heappop(max_heap)
            res_ratio+=(p/t)
        return (res_ratio/len(classes))