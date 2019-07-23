class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(i:int)->bool:
            k = abs(i)
            while k>0:
                r = k%10
                if r==0:
                    return False
                if i%r!=0:
                    return False
                k = k//10           
            return True
        
        A = []
        for i in range(left, right+1):
            if check(i):
                A.append(i)
        return A
    