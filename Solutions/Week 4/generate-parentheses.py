class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ls = []
        self.generate(0,0,n, ls, "")
        return ls
        
    def generate(self, op, close, n, ls, S):
        if (op==n and close==n):
            ls.append(S)
        if (op>close and close<n):
            self.generate(op, close+1, n, ls, S+')')
        if (op<n):
            self.generate(op+1, close, n, ls, S+'(')
