# Recursive, but times out in python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        if word1[0]==word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            return 1+min(self.minDistance(word1[1:], word2[1:]),
                         self.minDistance(word1, word2[1:]),
                         self.minDistance(word1[1:], word2))