class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
         # MY CODE TOO LENGTHY AND LESS OPTIMAL 
        # diag=[]
        # nondiag=[]
        # start=0
        # end=len(grid)-1
        # for i in range (0,end+1):
        #     diag.append(grid[i][i])
        # for i in range(end,-1,-1):
        #     diag.append(grid[i][abs(i-end)])
        # for i in range(0,end+1):
        #     for j in range(0,end+1):
        #         if(i!=j and j!=abs(i-end)):
        #             nondiag.append(grid[i][j])
        # setofnondiag=set(nondiag)
        # print(diag)
        # print(setofnondiag)
        # if ((0 not in diag)and(len(setofnondiag)==1 and (0 in setofnondiag))):
        #     return True 
        # return False  

        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True     