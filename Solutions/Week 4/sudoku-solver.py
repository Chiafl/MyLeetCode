class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        horizontalSet = [set() for i in range(len(board))]
        verticalSet = [set() for j in range(len(board[0]))]
        blockSet = [[set() for l in range(len(board)//3) ] for k in range(len(board)//3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j].isnumeric()):
                    horizontalSet[i].add(board[i][j])
                    verticalSet[j].add(board[i][j])
                    blockSet[i//3][j//3].add(board[i][j])
        self.solve(board, 0, 0, horizontalSet, verticalSet, blockSet)
        
    def solve(self, board, i, j, hSet, vSet, bSet):
        if (j>=len(board[0])):
            i = i+1
            j = 0
            
        if (i>=len(board)):
            return True
        
        if (board[i][j].isnumeric()):
            return self.solve(board, i, j+1, hSet, vSet, bSet)
        else:
            for num in range(1,10):
                c = str(num)
                if c in hSet[i] or c in vSet[j] or c in bSet[i//3][j//3]:
                    continue
                board[i][j] = c
                hSet[i].add(c)
                vSet[j].add(c)
                bSet[i//3][j//3].add(c)
                if (self.solve(board, i, j+1, hSet, vSet, bSet)):
                    return True                
                hSet[i].remove(c)
                vSet[j].remove(c)
                bSet[i//3][j//3].remove(c)
                board[i][j] = '.'
        return False
                
                