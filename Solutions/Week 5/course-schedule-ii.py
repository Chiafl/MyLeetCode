from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        Q = deque()
        visited = 0
        outgoing = defaultdict(list)
        incoming = [0 for i in range(numCourses)]
        order = []
        for pre in prerequisites:
            if pre[1] not in outgoing:
                outgoing[pre[1]] = [pre[0]]
            else:
                outgoing[pre[1]].append(pre[0])
            incoming[pre[0]] += 1
        for i in range(numCourses):
            if incoming[i]==0:
                Q.append(i)
                order.append(i)
        while Q:
            curr = Q.popleft()
            visited +=1
            for out in outgoing[curr]:
                incoming[out] -= 1
                if incoming[out] == 0:
                    Q.append(out)
                    order.append(out)
        if visited != numCourses:
            return []
        return order
        
        
