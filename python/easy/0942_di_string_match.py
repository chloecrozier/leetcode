# https://leetcode.com/problems/di-string-match/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        dCount = len(s)
        iCount = 0
        res = []
        for c in s:
            if c == 'I':
                res.append(iCount)
                iCount += 1
            else:
                res.append(dCount)
                dCount -= 1

        res.append(iCount)
        return res
