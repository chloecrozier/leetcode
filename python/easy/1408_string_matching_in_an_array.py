# https://leetcode.com/problems/string-matching-in-an-array/description/?envType=daily-question&envId=2025-01-07
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        superWord = ''
        res = []
        for w in words:
            superWord += w
            superWord += ' '

        for w in words:
            if superWord.count(w) > 1:
                res.append(w)

        return res
