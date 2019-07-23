class Solution:
    def isHappy(self, n: int) -> bool:
        S = set()
        while (n!=1):
            if n not in S: 
                S.add(n)
            else:
                return False
            v = 0
            while (n>0):
                v += pow(n%10,2)
                n //= 10
            n = v
        return True