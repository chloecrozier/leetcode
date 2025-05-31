# https://leetcode.com/problems/maximum-odd-binary-number/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        numOnes = s.count('1')
        res = ['0'] * len(s)
        if numOnes == 1:
            return "".join((['0'] * (len(s) - 1)) + ['1'])
        else:
            res[-1] = '1'
            for i in range(numOnes - 1):
                res[i] = '1'
            return "".join(res)
