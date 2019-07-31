# My solution is based on fact that if you can color a graph with 2 colors, then it is bipartite
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False]*(len(graph))
        color = [False]*(len(graph))
        for i, g in enumerate(graph):
            if visited[i]:
                continue
            # (Node id, neighbor nodes, initialized with color)
            stack = [(i, graph[i], True)]
            while stack:
                curr = stack.pop()
                # continue if visited and same color, exit if sequential colors
                if visited[curr[0]]:    
                    if curr[2]!=color[curr[0]]:
                        return False
                    continue
                visited[curr[0]] = True
                color[curr[0]] = curr[2]
                for edgeNode in curr[1]:
                    # Push onto each neighbor nodes with alternate color to stack
                    stack.append((edgeNode, graph[edgeNode], not curr[2]))
        return True