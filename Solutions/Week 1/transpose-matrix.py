class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if len(A)==0:
            return A
        B = []
        for i in range(0, len(A[0])):
            B.append([A[j][i] for j in range(0, len(A))])
        return B