class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        visited = [[0 for a in range(len(matrix[0]))] for b in range(len(matrix))]
        self.ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if visited[i][j]==0:
                    self.val = float('-inf')
                    self.backtrack(matrix, i, j, 1, visited, float('-inf'))
                    self.ans = max(self.val, self.ans)
        return self.ans
                
    def backtrack(self, matrix, i, j, val, visited, prev):
        if matrix[i][j]<=prev or val<=visited[i][j]:
            return
        visited[i][j] = val
        if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
            self.backtrack(matrix, i-1, j, val+1, visited, matrix[i][j])
        if j-1>=0 and matrix[i][j-1]>matrix[i][j]:
            self.backtrack(matrix, i, j-1, val+1, visited, matrix[i][j])
        if i+1<len(matrix) and matrix[i+1][j]>matrix[i][j]:
            self.backtrack(matrix, i+1, j, val+1, visited, matrix[i][j])
        if j+1<len(matrix[0]) and matrix[i][j+1]>matrix[i][j]:
            self.backtrack(matrix, i, j+1, val+1, visited, matrix[i][j])
        self.val = max(val, self.val)
        return