# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
class Solution(object):
    def getAncestors(self, n, edges):
        ancestors = [[] for _ in range(n)]
        for edge in edges:
            ancestors[edge[1]].append(edge[0])

        def dfs(node, visited):
            for ancestor in ancestors[node]:
                if ancestor not in visited:
                    visited.add(ancestor)
                    dfs(ancestor, visited)

        res = [[] for _ in range(n)]
        for i in range(n):
            visited = set()
            dfs(i, visited)
            res[i] = sorted(visited)

        return res
