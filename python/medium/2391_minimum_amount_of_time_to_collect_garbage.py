# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = len("".join(garbage))
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        travel = [0] + travel
        
        g = 0
        p = 0
        m = 0
        for i in range(len(garbage) - 1, -1, -1):
            if "G" in garbage[i] and g == 0:
                res += travel[i]
                g = 1
            if "M" in garbage[i] and m == 0:
                res += travel[i]
                m = 1
            if "P" in garbage[i] and p == 0:
                res += travel[i]
                p = 1

        return res
