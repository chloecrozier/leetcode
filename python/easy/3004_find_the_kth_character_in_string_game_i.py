# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/
class Solution:
    def incrementStr(self, s: str) -> str:
        res = ''
        for c in s:
            res += self.incrementChr(c)
        return res

    def incrementChr(self, c: str) -> str:
        return chr(((ord(c) + 1 - ord('a')) % 26) + ord('a'))

    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            word += self.incrementStr(word)
        return word[k - 1]
