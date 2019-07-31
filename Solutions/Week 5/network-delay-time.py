import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        vertices = [Vertex(n) for n in range(N)]
        for t in times:
            vertices[t[0]-1].addEdge(t[1]-1,t[2])
        visited = [False]*N
        Q = [(0, K-1)]
        time = 0
        highest = float('-inf')
        while Q:
            curr = heapq.heappop(Q)
            if visited[curr[1]]:
                continue
            visited[curr[1]] = True
            highest = max(highest, curr[0])
            for v in vertices[curr[1]].edge:
                heapq.heappush(Q,(curr[0]+v[1], v[0]))
        if all(visited):
            return highest
        return -1
            
        
class Vertex:
    def __init__(self,vertex:int):
        self.id = vertex
        self.edge = []
        
    def addEdge(self, vertex:int, time:int):
        self.edge.append((vertex, time))