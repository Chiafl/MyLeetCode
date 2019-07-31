class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        for p in prerequisites:
            d[p[1]] = d.get(p[1],[])+[p[0]]
        print(d)
        for item in d.items():
            visited = [False for i in range(numCourses)]
            visited[item[0]] = True
            stack = item[1]
            while stack:
                curr = stack.pop()
                if (curr==item[0]):
                    return False
                if (visited[curr]):
                    continue
                visited[curr] = True
                if (curr in d):
                    for i in d[curr]:
                        stack.append(i)
        return True