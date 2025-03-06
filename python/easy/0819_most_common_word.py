# https://leetcode.com/problems/most-common-word/description/
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        res = ''
        maxCount = 0
        m = {}
        for w in banned:
            m[w] = -1

        for w in re.split(r'[ ,.!?;\']+', paragraph):
            w = w.lower()
            if w in m:
                if m[w] != -1:
                    m[w] += 1
                    if m[w] > maxCount:
                        maxCount = m[w]
                        res = w
            else:
                m[w] = 1
                if m[w] > maxCount:
                        maxCount = m[w]
                        res = w
        
        return res
