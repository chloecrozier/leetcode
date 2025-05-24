# https://leetcode.com/problems/find-words-containing-character/description/?envType=daily-question&envId=2025-05-24
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            for c in words[i]:
                if c == x:
                    res.append(i)
                    break
        return res
