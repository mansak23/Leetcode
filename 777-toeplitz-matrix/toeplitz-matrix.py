class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            # m=set()
            for j in range(len(matrix[0])):
                m=set()
                m.add(matrix[i][j])
                if (i+1 <len(matrix)) and (j+1 < len(matrix[0])):
                    if matrix[i+1][j+1] not in m:
                        return False
                    else:
                        m.add(matrix[i+1][j+1])
                print(m)
        return True
