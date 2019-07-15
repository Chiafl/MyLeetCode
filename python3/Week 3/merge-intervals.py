# Merge sort didn't time out but built in sort was 30x faster 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or not intervals[0]:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0]) #self.part(intervals)
        ls = []
        for i,(x,y) in enumerate(intervals):
            if i == 0:
                ls.append([x,y])
            else:
                if x<=ls[-1][1]:
                    ls[-1][1] = max(ls[-1][1],y)
                else:
                    ls.append([x,y])
        return ls
        
    def part(self, I: List[List[int]]):
        if len(I)<=1:
            return I
        n = len(I)//2
        return self.mergeInterval(self.part(I[0:n]),self.part(I[n:]))
    
    def mergeInterval(self, I1: List[List[int]], I2: List[List[int]]):
        if not I1:
            return I2
        if not I2:
            return I1
        if I1[0][0]<I2[0][0]:
            return [I1[0]]+self.mergeInterval(I1[1:], I2)
        elif I1[0][0]>I2[0][0]:
            return [I2[0]]+self.mergeInterval(I1, I2[1:])
        else:
            if I1[0][1]<I2[0][1]:
                return [I1[0]]+self.mergeInterval(I1[1:], I2)
            else:
                return [I2[0]]+self.mergeInterval(I1, I2[1:])
