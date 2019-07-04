class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for x, y in zip(s,t):
            if x not in d.keys() and y not in d.values():
                d[x] = y
            elif x in d.keys() and d[x]==y:
                continue
            else:
                return False
        return True
        