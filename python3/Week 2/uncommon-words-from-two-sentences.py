import collections

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        setAB = collections.Counter(A.split(" "))+collections.Counter(B.split(" "))
        return [elem for elem in setAB if setAB[elem]==1]
        