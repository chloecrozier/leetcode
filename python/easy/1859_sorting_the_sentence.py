# https://leetcode.com/problems/sorting-the-sentence/description/
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        res = [''] * len(s)
        for word in s:
            place = int(word[-1])
            res[place - 1] = word[:-1]
        return ' '.join(res)
