class Solution:
    def findComplement(self, num: int) -> int:
        n = num
        cnt = 0
        while n>0:
            n//=2
            cnt+=1
        return num^((1<<cnt)-1)
            
            