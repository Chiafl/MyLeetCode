class Solution:
    def titleToNumber(self, s: str) -> int:
        val = 0
        for i in range(1,len(s)+1):
            val = val+(ord(s[-i])-64)*26**(i-1) 
        return val