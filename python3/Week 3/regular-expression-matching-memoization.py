class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)
        arr = [[False for i in range(n+1)] for j in range(m+1)]
        for i in range(n):
            if p[i]=='*':
                if i==1:
                    arr[0][i+1] = True
                else:
                    arr[0][i+1] = arr[0][i-1]
            else:
                arr[0][i+1] = False
        arr[0][0] = True
        for i in range(m):
            for j in range(n):
                if (p[j]==s[i] or p[j]=='.'):
                    arr[i+1][j+1] = arr[i][j]
                elif p[j]=='*': 
                    if p[j-1]==s[i] or p[j-1]=='.':
                        arr[i+1][j+1] = arr[i][j+1]
                    arr[i+1][j+1] = arr[i+1][j+1] or arr[i+1][j-1]
                else:
                    arr[i+1][j+1]= False
        return arr[-1][-1]