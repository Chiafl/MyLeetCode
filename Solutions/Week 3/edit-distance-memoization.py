class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        arr = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(len(arr)):
            arr[i][0] = i
        for j in range(len(arr[0])):
            arr[0][j] = j
        arr[0][0] = 0
        for i in range(len(arr)-1):
            for j in range(len(arr[0])-1):
                if word1[i]==word2[j]:
                    arr[i+1][j+1] = arr[i][j]
                else:
                    arr[i+1][j+1] = 1+min(min(arr[i][j],arr[i+1][j]), arr[i][j+1])
        return arr[-1][-1]
