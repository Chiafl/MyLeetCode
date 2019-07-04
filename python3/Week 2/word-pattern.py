class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = dict()
        ls = str.split(" ")
        if len(pattern)!=len(ls): return False
        for x,y in zip(pattern, ls):
            if x not in d.keys() and y not in d.values():
                d[x] = y
            elif x in d.keys() and d[x]==y:
                continue
            else:
                return False
        return True