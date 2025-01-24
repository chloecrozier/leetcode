# https://leetcode.com/problems/find-eventual-safe-states/description/?envType=daily-question&envId=2025-01-24
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        m = {}
        q = []
        res = []
        inCount = [0] * len(graph) 

        for i in range(len(graph)):
            inCount[i] = len(graph[i])
            if len(graph[i]) == 0:
                q.append(i)
            for node in graph[i]:
                if node in m:
                    m[node].append(i)
                else:
                    m[node] = [i]

        while q:
            curr = q.pop(0)
            res.append(curr)
            if curr in m:
                for node in m[curr]:
                    inCount[node] -= 1
                    if inCount[node] == 0:
                        q.append(node)

        return sorted(res)
