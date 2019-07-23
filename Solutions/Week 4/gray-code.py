class Solution:
    def grayCode(self, n: int) -> List[int]:
        ls = [0]
        self.helper(0, n, ls)
        return ls
        
    def helper(self, k, n, ls):
        if k>=n:
            return
        prev = ls[-1]
        for i in range(n):
            temp = prev^(1<<i)
            if temp not in ls:
                ls.append(temp)
                self.helper(k, n, ls)