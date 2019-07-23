class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        parent = 0
        value = 0
        for i, s in enumerate(S):
            if s=='(':
                parent+=1
            else:
                parent-=1
                if S[i-1]=='(':
                    value+=pow(2,parent)
        return value
            