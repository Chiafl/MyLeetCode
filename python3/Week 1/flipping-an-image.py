class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
        return [list(map(lambda x: x^1, row)) for row in A]
        