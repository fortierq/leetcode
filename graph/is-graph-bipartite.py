class Solution:
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(v, c):
            if color[v] == 1 - c:
                return False
            if color[v] != -1:
                return True
            color[v] = c
            for w in graph[v]:
                if not dfs(w, 1 - c):
                    return False
            return True

        for v in range(n):
            if color[v] == - 1 and not dfs(v, 1):
                return False
        return True
