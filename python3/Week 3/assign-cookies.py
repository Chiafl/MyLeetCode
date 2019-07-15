class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        cnt = 0
        while g and s:
            if s[-1]>=g[-1]:
                g.pop()
                s.pop()
                cnt+=1
            else:
                g.pop()
        return cnt