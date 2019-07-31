class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0]==board[i][j]:
                    visited = [[False for a in range(len(board[0]))] for b in range(len(board))]
                    if (self.backtrack(board, word, visited, 0, i, j)):
                        return True
        return False
    
    def backtrack(self, board, word, visited, index, i, j):
        if index>=len(word):
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or visited[i][j]:
            return False
        if word[index]==board[i][j]:
            visited[i][j] = True
            if (self.backtrack(board, word, visited, index+1, i+1, j)
                or self.backtrack(board, word, visited, index+1, i-1, j)
                or self.backtrack(board, word, visited, index+1, i, j-1)
                or self.backtrack(board, word, visited, index+1, i, j+1)
               ):
                return True
            visited[i][j] = False
        return False