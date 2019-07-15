class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, 0, 0)
    
    def helper(self, s, p, sIndex, pIndex):
        if sIndex>=len(s) and pIndex>=len(p):
            return True
        
        if sIndex>=len(s) or pIndex>=len(p):
            if pIndex>=len(p):
                return False
            else:
                if pIndex+1<len(p) and p[pIndex+1]=='*':
                    return self.helper(s, p, sIndex, pIndex+2)
                else:
                    return False
                        
        if pIndex+1<len(p) and p[pIndex+1]=='*':
            if p[pIndex]==s[sIndex] or p[pIndex] == '.':
                return (self.helper(s, p, sIndex+1, pIndex) 
                    or self.helper(s, p, sIndex, pIndex+2))
            else:
                return self.helper(s, p, sIndex, pIndex+2)
            
        if p[pIndex]==s[sIndex] or p[pIndex] == '.':
            return self.helper(s, p, sIndex+1, pIndex+1) 
            
        return False