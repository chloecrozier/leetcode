# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=daily-question&envId=2025-03-02
class Solution:
    def mergeArrays(self, n1: List[List[int]], n2: List[List[int]]) -> List[List[int]]:
        m = {}
        res = []
        i = 0
        j = 0
        while i < len(n1) and j < len(n2):
            if n1[i][0] < n2[j][0]:
                if n1[i][0] in m:
                    m[n1[i][0]] += n1[i][1]
                else:
                    m[n1[i][0]] = n1[i][1]
                    res.append([n1[i][0], -1])
                i += 1
            elif n1[i][0] > n2[j][0]:
                if n2[j][0] in m:
                    m[n2[j][0]] += n2[j][1]
                else:
                    m[n2[j][0]] = n2[j][1]
                    res.append([n2[j][0], -1])
                j += 1
            else:
                m[n1[i][0]] = n1[i][1] + n2[j][1]
                res.append([n1[i][0], -1])
                i += 1
                j += 1
        
        for entry in res:
             entry[1] = m[entry[0]]

        if i < len(n1):
            res.extend(n1[i:])
        if 2 < len(n2):
            res.extend(n2[j:])

        return res
