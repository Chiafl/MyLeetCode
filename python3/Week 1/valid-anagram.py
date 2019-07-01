# Tried just for fun wondering whether python comparator operator ==
# compares objects' addresses or objects' properties 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        S = {}
        T = {}
        for a in s:
            if a in S:
                S[a]=S[a]+1
            else:
                S[a]=1
        for b in t:
            if b in T:
                T[b]=T[b]+1
            else:
                T[b]=1
        return S==T
        
        