# https://leetcode.com/problems/count-servers-that-communicate/description/?envType=daily-question&envId=2025-01-23
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = {}
        serverNum = 0
        singular = 0
        seen = {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    serverNum += 1

                    if r in m:
                        m[r].append(serverNum)
                    else:
                        m[r] = [serverNum]

                    if 1000 + c in m:
                        m[1000 + c].append(serverNum)
                    else:
                        m[1000 + c] = [serverNum]

        for key, value in m.items():
            if len(value) == 1:
                if value[0] in seen:
                    singular += 1
                else:
                    seen[value[0]] = 1

        return serverNum - singular
