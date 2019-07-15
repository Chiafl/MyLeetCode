class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = ["",0]
        d = {}
        for i,s in enumerate(S):
            if s not in d:
                d[s] = [i,i]
            else:
                d[s][1] = i
        d = sorted(d.items(), key=lambda item: item[1][0])
        k = []
        for i,(x,y) in enumerate(d):
            if i>0:
                if y[0]>k[-1][1]:
                    k.append([y[0],y[1]])
                else:
                    k[-1][0] = min(y[0], k[-1][0])
                    k[-1][1] = max(y[1], k[-1][1])
            else:
                k.append([y[0],y[1]])
        return list(map(lambda elem: elem[1]-elem[0]+1, k))