import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        n = len(s)
        m = len(p)
        l = []
        sortP = collections.Counter(p)
        sortS = collections.Counter(s[:m])
        for i in range(n-m+1):
            if sortS==sortP:
                l.append(i)
            if (i+m<n):
                sortS[s[i]]-=1
                sortS[s[i+m]]+=1
                if sortS[s[i]]==0:
                    del sortS[s[i]]
        return l