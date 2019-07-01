class Solution:
    def binaryGap(self, N: int) -> int:
        cnt = 0
        maximum = 0
        b = True
        while N>0:
            if N&1==1:
                if b:
                    b = False
                else:
                    maximum = max(cnt, maximum)
                cnt=1
            else:
                cnt+=1
            N>>=1
        return maximum
        