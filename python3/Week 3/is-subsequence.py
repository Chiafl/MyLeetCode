class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s)>len(t):
            return False
        i = 0 #pointer for s
        j = 0 #pointer for j
        while j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
                if i==len(s):
                    break
            else:
                j+=1
        return i==len(s)