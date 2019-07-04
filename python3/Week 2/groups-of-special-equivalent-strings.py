# Had a bit trouble with this one
# Realized halfway that I could just partition and sort 

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        S = set()
        for a in A:
            first = sorted([x for i,x in enumerate(a) if (i%2==0)])
            sec = sorted([x for i,x in enumerate(a) if (i%2==1)])
            S.add(str(first)+str(sec))
        return len(S)