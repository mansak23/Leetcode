class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res=[[] for _ in range(len(matrix))]
        for i in range (len(matrix)):
            for j in range (len(matrix)-1,-1,-1):
                res[i].append(matrix[j][i])
        for i in range(len(matrix)):
            matrix[i]=res[i]
        print(res)
