class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(' ')
        S = ""
        for l in ls:
            rev = ""
            for i in range(1, len(l)+1):
                rev += l[-i]
            S += rev+' ' 
        #return everything but the tail since it has whitespace
        return S[:-1]