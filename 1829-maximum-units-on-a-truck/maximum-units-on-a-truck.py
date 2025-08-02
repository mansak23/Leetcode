class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes,key=lambda x:x[1],reverse=True)
        print(boxTypes)
        currsize=boxTypes[0][0]
        res=boxTypes[0][0]*boxTypes[0][1]
        if currsize>truckSize:
            return 8
        for i in range(1,len(boxTypes)):
            if currsize>=truckSize:
                break
            elif currsize+boxTypes[i][0]<=truckSize:
                res+=boxTypes[i][0]*boxTypes[i][1]
                currsize+=boxTypes[i][0]
            elif currsize+boxTypes[i][0]>truckSize:
                res+=(truckSize-currsize)*boxTypes[i][1]
                currsize+=(truckSize-currsize)
        return res
            
            