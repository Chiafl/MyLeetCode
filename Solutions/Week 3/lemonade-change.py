class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            i-=5
            if i==0:
                five+=1
            elif i==5:
                if five<1:
                    return False
                five-=1
                ten+=1
            elif i==15:
                if ten>0 and i>0:
                    i-=10
                    ten-=1
                while i>0:
                    if five<1:
                        return False
                    i-=5
                    five-=1
                if i>0:
                    return False
        return True
                