class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        k = n
        while (k>=1):
            if k==1:
                return True
            k/=2
        return False