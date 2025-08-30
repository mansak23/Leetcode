class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board2=[[] for _ in range(9)]
        mat3x3=[[] for _ in range(9)]
        for i in range (9):
            for j in range(9):
                board2[i].append(board[j][i])
        for r in range(9):
            for c in range(9):
                matindex=(r//3)*3 + (c//3)
                mat3x3[matindex].append(board[r][c])
        # print(mat3x3)
        for i in range(9):
            l=set()
            t=set()
            b=set()
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in l:
                        return False
                if board2[i][j]!=".":
                    if board2[i][j] in t:
                        return False
                if mat3x3[i][j]!=".":
                    if mat3x3[i][j] in b:
                        return False
                l.add(board[i][j])
                t.add(board2[i][j])
                b.add(mat3x3[i][j])
            # print(l,t)
        return True