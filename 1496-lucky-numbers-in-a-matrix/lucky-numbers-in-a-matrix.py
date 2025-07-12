class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rowmin=[]
        for i in range(len(matrix)):
            rowmin.append(min(matrix[i]))
        column=[[] for _ in range (len(matrix[0]))]
        if (len(matrix) or len(matrix[0]))==0:
            return []
        for i in range(len(matrix)):        # rows
            for j in range(len(matrix[0])): # columns
                column[j].append(matrix[i][j])
        colmax=[]
        for i in range(len(column)):
            colmax.append(max(column[i]))
        for i in colmax:
            if i in rowmin:
                return [i]
        return []