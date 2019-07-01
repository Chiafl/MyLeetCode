class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        def visit(grid: List[List[str]], i: int, j: int):
            if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j]=='0' or grid[i][j]=='2':
                return
            grid[i][j] = '2'
            visit(grid, i-1, j)            
            visit(grid, i+1, j)
            visit(grid, i, j-1)            
            visit(grid, i, j+1)
            return
            
        v = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]!='0' and grid[i][j]!='2':
                    visit(grid, i, j)
                    v+=1
        return v