#This is a very inefficient method, but accepted
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def union(board: List[List[str]], i: int, j: int, sets: dict, setsCnt: int):
            sets[(i,j)]=setsCnt
            keys = sets.keys()
            if i-1>=0 and board[i-1][j]=='O' and (i-1, j) not in keys:
                union(board, i-1, j, sets, setsCnt)
            if j+1<len(board[0]) and board[i][j+1]=='O' and (i, j+1) not in keys:
                union(board, i, j+1, sets, setsCnt)
            if i+1<len(board) and board[i+1][j]=='O' and (i+1, j) not in keys:
                union(board, i+1, j, sets, setsCnt)
            if j-1>=0 and board[i][j-1]=='O' and (i, j-1) not in keys:
                union(board, i, j-1, sets, setsCnt)
            return
        
        if not board or not board[0]:
            return
        setsCnt = 1
        sets = {}
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if (i, j) in sets.keys() or board[i][j]=='X':
                    continue
                union(board, i, j, sets, setsCnt)
                setsCnt+=1
        delete = set()
        for i in range(0, len(board)):
            if (i, 0) in sets.keys():
                delete.add(sets[(i,0)])
            if  (i, len(board[0])-1) in sets.keys():
                delete.add(sets[(i, len(board[0])-1)])
        for j in range(0, len(board[0])):
            if (0, j) in sets.keys():
                delete.add(sets[(0,j)])
            if  (len(board)-1, j) in sets.keys():
                delete.add(sets[(len(board)-1,j)])
        for x, y in list(sets.items()):
            if y in delete:
                del sets[x]
        for (a,b), c in sets.items():
            board[a][b] = 'X'
        return