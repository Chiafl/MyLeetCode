class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        ls = [[-1 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(len(ls)):
            ls[i][0] = i
        for j in range(len(ls[0])):
            ls[0][j] = j
        self.helper(word1, word2, ls, 1, 1)
        return ls[-1][-1]
        
    def helper(self, word1, word2, ls, i, j):
        if i>=len(ls):
            return
        if j>=len(ls[0]):
            return
        if not word1 or not word2:
            ls[i][j] = max(len(word1), len(word2))
            return
        if word1[i-1]==word2[j-1]:
            ls[i][j] = ls[i-1][j-1]
        else:
            ls[i][j] = 1+min(ls[i-1][j-1],ls[i-1][j], ls[i][j-1])
        self.helper(word1, word2, ls, i, j+1)
        if (j==1):
            self.helper(word1, word2, ls, i+1, 1)
