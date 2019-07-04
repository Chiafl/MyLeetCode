import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]: return False
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                elem = board[i][j]
                if elem == '.': 
                    continue
                elif elem in rows[i] or elem in columns[j] or elem in square[(i//3*3)+j//3]:
                    return False
                rows[i].add(elem)
                columns[j].add(elem)
                square[(i//3*3)+j//3].add(elem)
        return True