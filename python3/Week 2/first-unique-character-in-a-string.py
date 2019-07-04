import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        C = collections.Counter(s)
        for x in C:
            if C[x]==1:
                return s.find(x)
        return -1