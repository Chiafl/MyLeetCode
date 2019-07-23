# Backtracking + Trie Implementation

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        T = Trie()
        for w in words:
            T.insert(w)
        truth = [[False for col in row] for row in board]
        S = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.backtrack(board, T, words, S, truth, i, j, "")
        return list(S)
        
    # Board, Trie, Words, Set, Index
    def backtrack(self, b, T, W, S, truth, i, j, s):
        if (i<0 or i>=len(b) or j<0 or j>=len(b[0]) or truth[i][j]):
            return False

        c = b[i][j]
        t = s
        s = s+c
        
        if s in W:
            S.add(s)
            T.word = False
                
        if c in T.d:
            truth[i][j] = True
            if j-1>=0:
                self.backtrack(b, T.d[c], W, S, truth, i, j-1, s)
            if j+1<len(b[0]):
                self.backtrack(b, T.d[c], W, S, truth, i, j+1, s)
            if i-1>=0:
                self.backtrack(b, T.d[c], W, S, truth, i-1, j, s)
            if i+1<len(b):
                self.backtrack(b, T.d[c], W, S, truth, i+1, j, s)
            truth[i][j] = False

class Trie:
    def __init__(self):
        self.d = {}
        self.word = False
        
    def insert(self, word):
        t = self
        for l in word:
            if l not in t.d:
                t.d[l] = Trie()
            t = t.d[l]
        t.word = True
        
    def search(self, word):
        t = self
        for l in word:
            if l not in t.d:
                return False
            t = t.d[l]
        return t.word
    
    def prefix(self, word):
        t = self
        for l in word:
            if l not in t.d:
                return False
            t = t.d[l]
        return t.word or bool(t.d)