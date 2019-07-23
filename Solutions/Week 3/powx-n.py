class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1/x
        y = self.myPow(x, n//2) if n>0 else self.myPow(x, -(-n//2))
        if n%2==1:
            return y*y*x if n>0 else y*y*(1/x)
        else:
            return y*y