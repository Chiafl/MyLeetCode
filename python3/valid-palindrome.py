#more efficient solution would be to use RegEx but str.replace doesn't support it

class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = s.lower()
        for i in range(0, len(S)):
            if not ((S[i]>='a' and S[i]<='z') or (S[i]>='0' and S[i]<='9')):
                S = (S[:i]+' '+S[i+1:]) if (i<len(S)) else (S[:i]+' ')
        S = S.replace(" ", "")
        for i in range(0, len(S)//2):
            if (S[i]!=S[len(S)-i-1]):
                return False
        return True