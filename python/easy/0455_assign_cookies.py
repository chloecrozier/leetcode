# https://leetcode.com/problems/assign-cookies/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        kid = len(g) - 1
        cookie = len(s) - 1

        res = 0
        while cookie >= 0 and kid >= 0:
            if s[cookie] >= g[kid]:
                cookie -= 1
                kid -= 1
                res += 1
            else:
                kid -= 1
            
        return res
