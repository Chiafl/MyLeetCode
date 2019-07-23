class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        v = 0
        for i in range(0, 32):
            if x&1 != y&1:
                v+=1
            x>>=1
            y>>=1
        return v