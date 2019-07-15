class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda x: x[0])
        ls = []
        for i,(x,y) in enumerate(points):
            if i>0:
                if x<=ls[-1][1]:
                    ls[-1][1] = min(y, ls[-1][1])
                    ls[-1][0] = max(x, ls[-1][0])
                else:
                    ls.append([x,y])
            else:
                ls.append([x,y])      
        print(ls)
        return len(ls)