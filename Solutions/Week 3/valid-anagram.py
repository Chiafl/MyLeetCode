class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.partition(s)==self.partition(t)
    
    def partition(self, s: str) -> str:
        if len(s)<=1:
            return s
        return self.merge(
            self.partition(s[0:len(s)//2]), 
            self.partition(s[len(s)//2:len(s)])
        )
    
    def merge(self, s1: str, s2: str) -> str:
        if not s2:
            return s1
        if not s1:
            return s2
        if s1[0]<s2[0]:
            return s1[0]+self.merge(s1[1:],s2)
        else:
            return s2[0]+self.merge(s1,s2[1:])